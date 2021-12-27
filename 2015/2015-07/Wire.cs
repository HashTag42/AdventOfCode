class Wire
{
    public string Name { get; init; }
    public ushort Value { get; set; }

    public bool HasValue { get; private set; }

    public Wire()
    {
        this.Name = "";
        this.Value = default;
        this.HasValue = false;
    }

    public Wire(string Name) => this.Name = Name;

    public void Set(ushort Value)
    {
        this.Value = Value;
        this.HasValue = true;
    }

    public void Reset()
    {
        this.Value = default;
        this.HasValue = false;
    }

    public override string ToString() => $"{this.Name}: {this.Value}";
}