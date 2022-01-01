class CaveMap
{
    /// PUBLIC CONSTRUCTORS

    public CaveMap(string FilePath) : this()
    {
        this.LoadMap(FilePath);
        this.PathCount = this.GetPathCount();
    }

    /// PUBLIC PROPERTIES

    public int PathCount { get; init; }

    public string CaveList => (String.Join(", ", this.Caves));

    /// PUBLIC METHODS

    public override string ToString()
    {
        string output = "";
        foreach(Cave cave in this.Caves) { output += cave.ToFullString() + Environment.NewLine; }
        return output;
    }

    /// PRIVATE CONSTRUCTORS

    private CaveMap()
    {
        this.Lines = new UniqueList<string>();
        this.Caves = new UniqueList<Cave>();
    }

    /// PRIVATE FIELDS
    private UniqueList<string> Lines { get; init; }

    private UniqueList<Cave> Caves { get; init; }

    /// PRIVATE METHODS

    private void LoadMap(string FilePath)
    {
        foreach(string line in File.ReadAllLines(FilePath))
        {
            this.Lines.Add(line);

            string[] subs = line.Split("-");

            Cave caveA = new Cave(subs[0]);
            Cave caveB = new Cave(subs[1]);

            this.Caves.AddIfNew(caveA);
            this.Caves.AddIfNew(caveB);

            this.Caves.Find(n => n == caveA).AddNeighbor(caveB);
            this.Caves.Find(n => n == caveB).AddNeighbor(caveA);
        }
        return;
    }

    private int GetPathCount()
    {
        int pathCount = 0;

        // TODO lol

        return pathCount;
    }

}
