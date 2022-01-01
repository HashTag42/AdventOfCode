class Cave: Node, IEquatable<Cave>
{
    /// CONSTRUCTORS

    public Cave(string Name) : base(Name)
    {
        if(Name == Name.ToLower())
        {
            this.Size = CaveSize.small;
        }
        else
        {
            this.Size = CaveSize.big;
        }
    }

    /// PUBLIC PROPERTIES

    public enum CaveSize { small, big }

    public CaveSize Size { get; init; }

    /// PUBLIC METHODS

    // The following methods are required to support the IEquatable interface.
    public bool Equals(Cave Other) => (this.Name == Other.Name);

    public override bool Equals(object obj) => this.Equals(obj);

    public override int GetHashCode() => this.Name.GetHashCode();

    public static bool operator == (Cave CaveA, Cave CaveB) =>   CaveA.Equals(CaveB);

    public static bool operator != (Cave CaveA, Cave CaveB) => !(CaveA.Equals(CaveB));

    /// PRIVATE METHODS

    /// PRIVATE FIELDS

}
