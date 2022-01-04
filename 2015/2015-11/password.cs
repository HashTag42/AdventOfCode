using System.Diagnostics;

class Password
{
    private int MinLength = 8;
    private int MaxLength = 8;
    private string InvalidCharacters = "ilo";
    private string CurrentPassword { get; set; }

    public Password(string CurrentPassword)
    {
        this.CurrentPassword = CurrentPassword;
    }

    public string GetNextPassword()
    {
        string nextPassword = this.CurrentPassword;

        do
        {
            nextPassword = RotatePassword(nextPassword);

        } while (!PasswordIsValid(nextPassword));
        this.CurrentPassword = nextPassword;

        return nextPassword;
    }

    private string RotatePassword(string Password)
    {
        char[] tmp = Password.ToCharArray();

        for (int i = Password.Length - 1; i >= 0; i--)
        {
            tmp[i] = RotateLetter(tmp[i]);
            if (tmp[i] != 'a')
            {
                break;
            }
        }
        string newPassword = new string(tmp.ToArray());

        return newPassword;
    }

    private char RotateLetter(char Letter)
    {
        char nextLetter = ' ';

        if (Letter == 'z')
        {
            nextLetter = 'a';
        }
        else
        {
            nextLetter = (char)(Convert.ToUInt16(Letter) + 1);
        }

        return nextLetter;
    }

    private bool PasswordIsValid(string Password)
    {
        bool passwordIsValid = false;

        if (MeetsLengthRequirements(Password)
         && OnlyContainsValidCharacters(Password)
         && IncludesIncreasingStraight(Password)
         && ContainsTwoPairs(Password))
        {
            passwordIsValid = true;
        }

        return passwordIsValid;
    }

    // Corporate policy dictates that passwords must be exactly eight lowercase letter
    private bool MeetsLengthRequirements(string Password)
    {
        bool meetsLengthRequirements = false;

        if (this.MinLength <= Password.Length && Password.Length <= this.MaxLength)
        {
            meetsLengthRequirements = true;
        }

        return meetsLengthRequirements;
    }

    // Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters
    // and are therefore confusing.
    private bool OnlyContainsValidCharacters(string Password)
    {
        bool invalidCharactersFound = false;

        foreach (char c in this.InvalidCharacters)
        {
            if (Password.Contains(c))
            {
                invalidCharactersFound = true;
                break;
            }
        }

        return !invalidCharactersFound;
    }

    // Passwords must include one increasing straight of at least three letters,
    // like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    private bool IncludesIncreasingStraight(string Password)
    {
        bool includesIncreasingStraight = false;

        for (int i = 0; i < Password.Length - 2; i++)
        {
            if (Password[i + 1] == (char)(Convert.ToUInt16(Password[i]) + 1)
             && Password[i + 2] == (char)(Convert.ToUInt16(Password[i]) + 2))
            {
                includesIncreasingStraight = true;
                break;
            }
        }

        return includesIncreasingStraight;
    }

    // Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
    private bool ContainsTwoPairs(string Password)
    {
        bool containsTwoPairs = false;

        int foundPairs = 0;
        for (int i = 0; i < Password.Length - 1; i++)
        {
            if (Password[i] == Password[i + 1])
            {
                foundPairs++;
                i++;
            }
        }

        if (foundPairs >= 2)
        {
            containsTwoPairs = true;
        }

        return containsTwoPairs;
    }

}