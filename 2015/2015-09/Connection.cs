class Connection
{
    public string CityA { get; init; }
    public string CityB { get; init; }
    public int Distance { get; init; }

    public Connection(string Line)
    {
        string[] subs = Line.Split("=", StringSplitOptions.TrimEntries);
        this.Distance = int.Parse(subs[1]);

        string[] cities = subs[0].Split("to", StringSplitOptions.TrimEntries);

        this.CityA = cities[0];
        this.CityB = cities[1];
    }

    public Connection(string CityA, string CityB, int Distance)
    {
        this.CityA    = CityA;
        this.CityB    = CityB;
        this.Distance = Distance;
    }

    public override string ToString() => this.CityA + " <-> " + this.CityB + " = " + this.Distance;
}