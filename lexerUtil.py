
string = '''
public class Test {

   public static void main(String args[]) {
      int [] numbers = {10, 20, 30, 40, 50};
      // printing !
      for(int x : numbers ) {
         System.out.print( x );
         System.out.print(",");
      }
      System.out.print("\n");
      String [] names = {"James", "Larry", "Tom", "Lacy"};
      /*
      looping over 
      */
      for( String name : names ) {
         System.out.print( name );
         System.out.print(",");
      }
   }
}
'''

symbols = ['{', '}', '(', ')', '[', ']', '.', '"', '*', '\n', ':', ','] # single-char keywords
other_symbols = ['\\', '/*', '*/'] # multi-char keywords
keywords = ['public', 'class', 'void', 'main', 'String', 'int']
KEYWORDS = symbols + other_symbols + keywords


white_space = ' '
lexeme = ''

for i,char in enumerate(string):
    if char == '*':
        if string[i-1] == '/':
            lexeme += '/*'
        elif string[i+1] == '/':
            lexeme += '*/'
        else:
            lexeme += '*'
    elif char == '/':
        if string[i+1] != '*' and string[i-1] != '*':
            lexeme += '/'
        else:
            continue
    else:
        if char != white_space:
            lexeme += char # adding a char each time
    if (i+1 < len(string)): # prevents error
        if string[i+1] == white_space or string[i+1] in KEYWORDS or lexeme in KEYWORDS: # if next char == ' '
            if lexeme != '':
                print(lexeme.replace('\n', '<newline>'))
                lexeme = ''
