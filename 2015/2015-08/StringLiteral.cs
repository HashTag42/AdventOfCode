using System.Diagnostics;

class StringLiteral
{
    public int CharactersOfCode   { get; init; }

    public int CharactersInMemory { get; init; }

    public int EncodedCharacters  { get; init; }

    public StringLiteral(string Line)
    {
        this.CharactersOfCode = Line.Length;

        // Account for the leading and trailing double quotes.
        this.EncodedCharacters += 4;

        for(int i = 1; i < Line.Length - 1; i++ )
        {
            if(Line[i].ToString() == @"\")
            {
                i++;
                switch(Line[i].ToString())
                {
                    case "\\":
                    case "\"":
                        this.EncodedCharacters +=2;
                        break;
                    case @"x":
                        this.EncodedCharacters += 1;
                        i += 2;
                        break;
                }
            }
            this.CharactersInMemory++;
        }
    }
}