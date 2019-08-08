# A Tic-Tac-Toe Board

theBoard={'t-l':'t-l','t-m':'t-m','t-r':'t-r',
          'm-l':'m-l','m-m':'m-m','m-r':'m-r',
          'l-l':'l-l','l-m':'l-m','l-r':'l-r'}
def printBoard(board):
           
           """This function prints out the board"""
           
           print(board['t-l']+' | '+board['t-m']+' | '+board['t-r'])
           print(' -- + --  + -- ')
           print(board['m-l']+' | '+board['m-m']+' | '+board['m-r'])
           print(' -- + --  + -- ')
           print(board['l-l']+' | '+board['l-m']+' | '+board['l-r'])
           
def winner(theBoard):
           
           """This function checks the winner"""
           for x in ['t','m','l']:        
           
                      if theBoard[x+'-l']==theBoard[x+'-m'] and theBoard[x+'-m']== theBoard[x+'-r']:
                                 print('The winner is '+theBoard[x+'-l'])
                                 return 1
                                 

           for y in ['l','m','r']:         
                      if theBoard['t-'+y]==theBoard['m-'+y] and theBoard['m-'+y]== theBoard['l-'+y]:
                                 print('The winner is '+theBoard['l-'+y])
                                 return 1
                                 
           
                      
           if theBoard['t-l']==theBoard['m-m'] and theBoard['m-m']== theBoard['l-r']:
                      print('The winner is '+theBoard['m-m'])
                      return 1
                      
                      
           if theBoard['t-r']==theBoard['m-m'] and theBoard['m-m']== theBoard['l-l']:
                      print('The winner is '+theBoard['m-m'])
                      return 1
           


print("***RULES***\nTo make a move use t,m,l as Top,Mid,Low and l,m,r as Left,Mid,Right in this format" + " 'm-m' for Mid-Mid or 't-l' for Top-Left.")
turn=input('\nWho wants to play first? X or O? : ')
turn=" "+turn+" "

while True:
           
           printBoard(theBoard)

           
           print('Turn for ' + turn +'. Move on which space?')
           move=input('Please enter your desired move: ')
                      
           theBoard[move]=turn
           if turn==' X ':
                      turn=' O '
           else:
                      turn=' X '

           flag=winner(theBoard)
           
           if flag==1:
                      winner(theBoard)
                      break

           
          
