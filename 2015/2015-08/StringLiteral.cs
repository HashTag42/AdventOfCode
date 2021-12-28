using System.Diagnostics;

class StringLiteral
{
    public int CharactersOfCode { get; private set; }

    public int CharactersInMemory { get; private set; }

    public StringLiteral() { }

    public StringLiteral(string Line) : this()
    {
        this.CharactersOfCode = Line.Length;

        for(int i = 1; i < Line.Length - 1; i++ )
        {
            if(Line[i].ToString() == @"\")
            {
                i++;
                switch(Line[i].ToString())
                {
                    case "\\":
                    case "\"":
                        break;
                    case @"x":
                        i += 2;
                        break;
                }
            }
            this.CharactersInMemory++;
        }
    }
}