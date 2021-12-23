/// This class represents a link between two caves.
/// The link is bidirectional.

class CaveLink
{
    /// This property represents the first cave in the link.
    public Cave A { get; init; }

    /// This property represents the scond cave in the link.
    public Cave B { get; init; }

    /// This constructor initializes a link between two caves.
    public CaveLink(Cave A, Cave B)
    {
        this.A = A;
        this.B = B;
    }

    /// This method returns true if a given cave is part of the link.
    public bool Contains(Cave Cave) => (A == Cave || B == Cave) ? true : false;

    /// This methods provides with a string representation of the object.
    public override string ToString() => (A.Name + "-" + B.Name);
}