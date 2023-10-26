import random 



class Blackjack : 

    

    deck_value = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"K":10,"Q":10,"J":10,"T":10,"A":1}
    deck = []

    def __init__(self,fund=500):
        self.fund = fund
        self.player_dealt = []
        self.dealer_dealt = []


    @classmethod
    def get_cards(cls) :
        cls.suit =["\u2666","\u2665","\u2663","\u2660"]
        for coefficients, value in cls.deck_value.items():
            for suit in cls.suit:
                cls.deck.append(str(coefficients)+str(suit))
        return cls.deck


    def get_bet(self,starting) :
        place_bet = 0
        while 1 :
            if starting.lower() == "yes" :
                while 1 :
                    input_bet = input("Place your bet: ")
                    if  float(input_bet) <= 0 :
                        print("The minimum bet is $1.")
                    elif  float(input_bet)>self.fund :
                        print("You do not have sufficient funds")
                    else :
                        place_bet = float(input_bet)
                        break 
            break
        return place_bet




    def get_point(self,hand) : 
        point = 0
        nbr_as = 0
        for card in hand :
            card_value = card[0]
            point += self.deck_value[card_value]
            if card_value == "A" :
                nbr_as += 1
        while nbr_as > 0 and point <= 21:
            point += 10
            nbr_as -= 1
        return point
     
       

    def get_dealt(self) :  
        while self.fund > 0 :
            starting = input(f"You are starting with ${self.fund}.Would you like to play a hand? ")
            if starting.lower() != "yes" :
                print("Goodbye !")
                break
            bet = self.get_bet(starting)
            random.shuffle(Blackjack.deck)
            player_dealt = [random.choice(Blackjack.deck),random.choice(Blackjack.deck)]
            dealer_dealt = [random.choice(Blackjack.deck),random.choice(Blackjack.deck)]
            self.player_dealt = player_dealt
            self.dealer_dealt= dealer_dealt
            print(f"You are dealt: {player_dealt[0]},{player_dealt[1]}")
            print(f"The dealer is dealt: {dealer_dealt[0]},Unknown")
            player_total_point = self.get_point(player_dealt)
            dealer_total_point = self.get_point(dealer_dealt)
            if ((Blackjack.deck_value[player_dealt[0][0]] + Blackjack.deck_value[player_dealt[1][0]] == 21) and (Blackjack.deck_value[dealer_dealt[0][0]] + Blackjack.deck_value[dealer_dealt[1][0]]) != 21) :
                print(f"The dealer has: {','.join(dealer_dealt)}")
                gain = bet*1.5
                self.fund += gain
                print(f"Blackjack! You win ${gain}!") 
            elif ((Blackjack.deck_value[player_dealt[0][0]] + Blackjack.deck_value[player_dealt[1][0]] == 21) and (Blackjack.deck_value[dealer_dealt[0][0]] + Blackjack.deck_value[dealer_dealt[1][0]]) == 21) :
                self.fund += bet
                print("You tie. Your bet has been returned.")
            else :
                while 1 :
                    mise=input(f"Would you like to hit or stay? ")
                    if mise == "hit" :
                        random.shuffle(Blackjack.deck)
                        player_dealt_hit = random.choice(Blackjack.deck)

                        self.player_dealt.append(player_dealt_hit)
                        print(f"You are dealt: {player_dealt_hit}")
                        player_total_point = self.get_point(player_dealt)
                        print(f"You now have: {','.join(player_dealt)}")
                        if player_total_point > 21 :
                            print(f"Your hand value is over 21 and you lose ${float(bet)} :( ")
                            self.fund -= float(bet)
                            break
                    elif mise.lower() == "stay" :
                        print(f"The dealer has: {','.join(dealer_dealt)}")
                        while dealer_total_point < 17 :
                            random.shuffle(Blackjack.deck)
                            dealer_dealt_hit = random.choice(Blackjack.deck)
                            dealer_dealt.append(dealer_dealt_hit)
                            print(f"The dealer hits and is dealt: {dealer_dealt_hit}")
                            dealer_total_point = self.get_point(dealer_dealt)
                            print(f"The dealer has: {','.join(dealer_dealt)}")
                        if dealer_total_point >= 17 :
                            print(f"The dealer stays.")
                            if dealer_total_point > player_total_point :
                                print(f"The dealer wins, you lose ${float(bet)} :( ")
                                self.fund -=float(bet)
                                break
                            elif dealer_total_point < player_total_point :
                                print(f"You win ${float(bet)} :) ")
                                self.fund += 2*float(bet)
                                break
                            elif dealer_total_point > 21:
                                print(f"The dealer busts, you win ${float(bet)} :) ") 
                                self.fund += 2*float(bet)
                                break                          
                            elif dealer_total_point == player_total_point:
                                print(f"You tie. Your bet has been returned.")
                                self.fund += float(bet)
                                break         
                    else :
                        print("That is not a valid option.")
        if self.fund <= 0:
            print("You've ran out of money. Please restart this program to try again. Goodbye!")

    
if __name__ == "__main__" :
    print("Welcome to Blackjack!")
    while 1 :
        depot = input("How much do you want to put in your balance? ")
        if depot.isdigit() or isinstance(depot,float) and float(depot) >= 5000 :
            blackjack = Blackjack(float(depot)) 
            blackjack.get_cards()
            blackjack.get_dealt()
            break
        else : 
            print("Your amount is invalid.") 

    

            

        