class DumboOctopusCell: DumboOctopus
{
    public DumboOctopusCell(int Row, int Col, int Energy): base(Energy)
    {
        this.Row= Row;
        this.Col= Col;
    }

    public int Row { get; init; }
    public int Col { get; init; }

    public override string ToString()
    {
        return (base.ToString());
    }
}