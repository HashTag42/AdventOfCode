class Graph
{
    private List<string> Lines { get; init; }

    private List<Node> Nodes { get; init; }

    private int[,] Edges { get; set; }

    public Graph()
    {
        this.Lines = new List<string>();
        this.Nodes = new List<Node>();
        this.Edges = new int[0,0];
    }

    public Graph(string FilePath) : this()
    {
        this.LoadGraph(FilePath);
    }

    private void LoadGraph(string FilePath)
    {
        foreach(string line in File.ReadAllLines(FilePath))
        {
            this.Lines.Add(line);

            string[] subs = line.Split("-");

            Node nodeA = new Node(subs[0]);
            Node nodeB = new Node(subs[1]);

            this.AddNodeIfNew(nodeA);
            this.AddNodeIfNew(nodeB);

            Node thisNodeA = this.Nodes.Find(n => n == nodeA);
            Node thisNodeB = this.Nodes.Find(n => n == nodeB);

            thisNodeA.AddNeighbor(thisNodeB);
            thisNodeB.AddNeighbor(thisNodeA);
        }
        return;
    }


    private void AddNodeIfNew(Node Node)
    {
        // Nodes are only added once to the graph
        if(!this.Nodes.Contains(Node))
        {
            this.Nodes.Add(Node);
        }
        return;
    }

    public override string ToString()
    {
        string output = "";

        foreach(string line in this.Lines)
        {
            output += line + Environment.NewLine;
        }

        output += Environment.NewLine;

        foreach(Node node in this.Nodes)
        {
            output += node + Environment.NewLine;
        }

        return output;
    }

}
