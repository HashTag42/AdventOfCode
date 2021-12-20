public class InsertionRule
{
    public ElementPair Pair { get; init; }
    public char Element { get; init; }

    public InsertionRule(string Line)
    {
        string[] terms = Line.Split(" -> ");
        this.Pair = new ElementPair(terms[0].ToCharArray());
        this.Element = terms[1][0];
    }

    public override string ToString()
    {
        return (Pair + " -> " + Element);
    }
}
