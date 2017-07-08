# Άσκηση 16_1_template
# Κρίση εργασίας: (βαθμολόγηση όπως παρακάτω)
import random
import time

marker = {'Παίκτης 1': 'X', 'Παίκτης 2': 'O', }

def display_board(board):
    # 4 μονάδες    
    print('1   |2   |3')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('4   |5   |6')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('7   |8   |9')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    return None
    
    #εμφάνισε την κατάσταση της τρίλιζας
    #pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης

def choose_first(): # 2 μονάδες    
    klhrwsh=random.randint(0,1)    
    if klhrwsh == 0:
        return list(marker.keys())[0]
    else:                
        return list(marker.keys())[1]
    #κλήρωση για το ποιος θα παίξει πρώτος
    # επιστρέφει είτε 'Παίκτης 1' είτε 'Παίκτης 2'
    #pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης

def display_score(score):    
    for player, wins in score.items():
        print('Ο', player, 'έχει', wins, 'νίκες')    
    # 2 μονάδες
    #Τυπώνει το τελικό σκορ
    #pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης

def place_marker(board, marker, position):
    board[position]=marker    
    # 2 μονάδες
    #Τοποθετεί στη θέση position του board τον marker
    #pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or #Οριζόντια πάνω 
    (board[4] == mark and board[5] == mark and board[6] == mark) or # Οριζόντια στη μέση 
    (board[1] == mark and board[2] == mark and board[3] == mark) or # Οριζόντια κάτω 
    (board[7] == mark and board[4] == mark and board[1] == mark) or # Κάθετα αριστερά 
    (board[8] == mark and board[5] == mark and board[2] == mark) or # Κάθετα στη μέση 
    (board[9] == mark and board[6] == mark and board[3] == mark) or # Κάθετα δεξιά
    (board[7] == mark and board[5] == mark and board[3] == mark) or # Διαγώνια 
    (board[9] == mark and board[5] == mark and board[1] == mark)) # Διαγώνια 
    # 4 μονάδες *
    #επιστρέφει True αν το σύμβολο mark έχει σχηματίσει τρίλιζα
    #pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης

def board_check(board):
     for i in range(1, 10):
         if board[i]==' ':
             return False
     return True

    # 2 μονάδες
    #επιστρέφει True αν υπάρχουν ακόμη κενά τετράγωνα
    #pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης
 
def player_choice(board, turn): # 2 μονάδες *
    position=input('Διάλεξε απο το (1-9): ')    
    while position not in '1 2 3 4 5 6 7 8 9'.split() or board[int(position)] != ' ':
        position=input('Διάλεξε απο το (1-9): ')  
    return int(position)       
    # Ο Παίκτης turn επιλέγει τετράγωνο
    # Επιστρέφει έναν ακέραιο στο διάστημα [1,9]
    #pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης

def replay(): # 1 μονάδα
    print('Θες να ξανα παίξεις; (ναι ή οχι)')
    return input().lower().startswith('ν')
    # Ρωτάει τον χρήστη αν θέλει να ξαναπαίξει και επιστρέφει True αν ναι.
    #pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης

def next_player(turn): # 1 μονάδα
    if turn == 'Παίκτης 1':
        print('Σειρά του Παίκτη 2: (Ο)')
        return 'Παίκτης 2'
    else:
        print('Σειρά του Παίκτη 1: (Χ)')
        return 'Παίκτης 1'
    #επιστρέφει τον επόμενο παίκτη που πρέπει να παίξει
    #pass #ΠΡΟΣΟΧΗ η εντολή pass, θα πρέπει να
    #αφαιρεθεί με την υλοποίηση της συνάρτησης

def main():
    score = {} # λεξικό με το σκορ των παικτών
    print('Αρχίζουμε!\nΓίνεται κλήρωση ', end = '')
    for t in range(10):
        print(".", flush='True', end=' ')
        time.sleep(0.2)
    print()
    # η μεταβλητή turn αναφέρεται στον παίκτη που παίζει
    turn = choose_first() 
    print("\nΟ " + turn + ' παίζει πρώτος.')
    # η μεταβλητή first αναφέρεται στον παίκτη που έπαιξε πρώτος
    first = turn 
    game_round = 1 # γύρος παιχνιδιού
    while True:
        # Καινούργιο παιχνίδι
        # Δημιουργία λίστας 10 στοιχείων βλέπε μάθημα 2 σελ.7 σημειώσεων
        theBoard = [' '] * 10 
        # Αφήστε το πρώτο στοιχείο δηλαδή το theBoard[0] κενό έτσι ώστε 
        # το index να αντιστοιχεί στην ονοματοδότηση των τετραγώνων 
        game_on = True  #ξεκινάει το παιχνίδι
        while game_on:
            display_board(theBoard) #Εμφάνισε την τρίλιζα
            # ο παίκτης turn επιλέγει θέση
            position = player_choice(theBoard, turn)            
            # τοποθετείται η επιλογή του
            place_marker(theBoard, marker[turn], position) 
            if win_check(theBoard, marker[turn]): # έλεγχος αν νίκησε
                display_board(theBoard)
                print('Νίκησε ο '+ turn)
                score[turn] = score.get(turn, 0) + 1
                game_on = False
            # έλεγχος αν γέμισε το ταμπλό χωρίς νικητή
            elif board_check(theBoard): 
                display_board(theBoard)
                print('Ισοπαλία!')
                game_on = False
            else: # αλλιώς συνεχίζουμε με την κίνηση του επόμενου παίκτη
                turn = next_player(turn)
        if not replay():
            ending = ''
            if game_round>1 : ending = 'υς'
            print("Μετά {} γύρο{}".format(game_round, ending))
            display_score(score) # έξοδος ... τελικό σκορ
            break
        else :
            game_round += 1
            # στο επόμενο παιχνίδι ξεκινάει ο άλλος παίκτης
            turn = next_player(first) 
            first = turn
main()


