class LookAndSayNumber
{
    public LookAndSayNumber(string Seed)
    {
        this.Seed = Seed;
    }

    public string Iterate(uint Count)
    {
        string result = this.Seed;
        for (uint i = 0; i < Count; i++)
        {
            result = this.GetLookAndSay(result);
        }

        return result;
    }

    private string GetLookAndSay(string Input)
    {
        if (Input.Length < 1)
        {
            throw new ArgumentOutOfRangeException();
        }

        List<string> groups = new List<string>();

        char digit = Input[0];
        int count = 1;

        for (int i = 1; i < Input.Length; i++)
        {
            if (Input[i] != digit)
            {
                // Add the current group to the
                groups.Add(count.ToString() + digit);

                // Start a new group
                digit = Input[i];
                count = 0;
            }
            count++;
        }
        groups.Add(count.ToString() + digit);

        return String.Join("", groups);
    }

    private string Seed { get; init; }

}
