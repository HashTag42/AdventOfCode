enum NodeSize { small, big }

class Node : IEquatable<Node>
{
    public string Name { get; init; }

    public NodeSize Size { get; init; }

    public List<Node> Neighbors { get; init; }

    public Node()
    {
        this.Name      = "";
        this.Size      = default;
        this.Neighbors = new List<Node>();
    }

    public Node(string Name) : this()
    {
        this.Name = Name;
        this.Size = (Name.ToLower() == Name) ? NodeSize.small : NodeSize.big;
    }

    public void AddNeighbor(Node NeighborNode)
    {
        // Neighbors are only added once to the list
        if(!this.Neighbors.Contains(NeighborNode)) { this.Neighbors.Add(NeighborNode); }
    }

    public bool Equals(Node Other)
    {
        bool equals = false;
        if(this.Name == Other.Name) { equals = true; }
        return equals;
    }

    public override bool Equals(object obj) => this.Equals(obj);

    public override int GetHashCode() => this.Name.GetHashCode();

    public static bool operator == (Node NodeA, Node NodeB) =>  NodeA.Equals(NodeB);

    public static bool operator != (Node NodeA, Node NodeB) => !NodeA.Equals(NodeB);

    public override string ToString()
    {
        string output = "";
        string separator = ", ";
        output += $"{this.Name} ({this.Size}) : ";
        foreach(Node n in this.Neighbors)
        {
            output += n.Name + separator;
        }
        output = output.Remove(output.Length - separator.Length, separator.Length);
        return output;
    }
}
