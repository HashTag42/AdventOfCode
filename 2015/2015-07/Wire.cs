class Wire
{
    public string Name { get; init; }
    public ushort Value { get; private set; }

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

    public override string ToString() => $"{this.Name}: HasValue: {this.HasValue} Value: {this.Value}";
}