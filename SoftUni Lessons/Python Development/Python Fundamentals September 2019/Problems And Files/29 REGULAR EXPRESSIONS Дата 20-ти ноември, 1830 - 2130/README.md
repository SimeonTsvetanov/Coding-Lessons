<h1 align="center">REGULAR EXPRESSIONS</h1>

<hr>

<blockquote>
    <p>Дата: 20-ти ноември, 18:30 - 21:30</p>
</blockquote>

<br>

<p>
    Video from the Lection: <a href="https://www.youtube.com/watch?time_continue=1&v=gAIpY70xyb0&feature=emb_title">here</a>
</p>

<hr>

<h3>Simple Code Snipets (Cheat-sheet)</h3>

    .       - Any Character Except New Line
    \d      - Digit (0-9)
    \D      - Not a Digit (0-9)
    \w      - Word Character (a-z, A-Z, 0-9, _)
    \W      - Not a Word Character
    \s      - Whitespace (space, tab, newline)
    \S      - Not Whitespace (space, tab, newline)

    \b      - Word Boundary
    \B      - Not a Word Boundary
    ^       - Beginning of a String
    $       - End of a String

    []      - Matches Characters in brackets
    [^ ]    - Matches Characters NOT in brackets
    |       - Either Or
    ( )     - Group

    Quantifiers:
    *       - 0 or More
    +       - 1 or More
    ?       - 0 or One
    {3}     - Exact Number
    {3,4}   - Range of Numbers (Minimum, Maximum)
    
    EXAMPLES:
    
    ### Naming groups:
     - To create the group_with name: (?P<separator>[\.\-\/])
     - To reuse the group_with name: (?P=separator)
    
    ### Using the Start and end for numbers:
        prefix_pattern = r"(^|(?<=\s))"
        number_pattern = r"(?P<number>-?\d+([.]\d+)?)"
        suffix_pattern = r"($|(?=\s))"
        pattern = prefix_pattern + number_pattern + suffix_pattern

    #### Sample Regexs ####

    [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+ 
