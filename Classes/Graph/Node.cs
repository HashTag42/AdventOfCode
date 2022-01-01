class Node : IEquatable<Node>
{
    /// CONSTRUCTORS

    public Node(string Name) : this()
    {
        this.Name = Name;
    }

    /// PUBLIC PROPERTIES

    public string Name { get; init; }

    public UniqueList<Node> Neighbors { get; init; }

    /// PUBLIC METHODS

    // Adds a node to the list of nodes connected to this object.
    public void AddNeighbor(Node NeighborNode) => this.Neighbors.AddIfNew(NeighborNode);

    // Returns a string representation for the object.
    public override string ToString() => this.Name;

    public string ToFullString() => $"{this.Name}: " + String.Join(", ", Neighbors);

    /// The following methods are required to support the IEquatable interface.

    // Nodes are only compared by their name and not their other properties.
    public bool Equals(Node Other) => (this.Name == Other.Name);

    public override bool Equals(object obj) => this.Equals(obj);

    public override int GetHashCode() => this.Name.GetHashCode();

    public static bool operator == (Node NodeA, Node NodeB) =>   NodeA.Equals(NodeB);

    public static bool operator != (Node NodeA, Node NodeB) => !(NodeA.Equals(NodeB));

    /// PRIVATE METHODS

    private Node()
    {
        this.Name      = "";
        this.Neighbors = new UniqueList<Node>();
    }

    /// PRIVATE FIELDS

}
