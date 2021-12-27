enum CommandType { Signal, Not, And, Or, LShift, RShift }

class Command
{
    public CommandType Type { get; init; }

    public List<string> Terms { get; init; }

    public List<ushort> Values { get; init; }

    public string WireName { get; init; }

    public bool Processed { get; set; }

    private string Line { get; init; }

    /// Default constructor to initialize member properties and fields.
    public Command()
    {
        this.Type = default;
        this.Terms = new List<string>();
        this.Values = new List<ushort>();
        this.WireName = "";
        this.Processed = false;
        this.Line = "";
    }

    public Command(string Line) : this()
    {
        this.Line       = Line;
        string[] subs   = Line.Split(" -> ");
        this.WireName   = subs[1];

        string[] args = subs[0].Split(" ");

        if(1 == args.Length) // SIGNAL
        {
            this.Type  = CommandType.Signal;
            ushort number = default;
            if(ushort.TryParse(args[0], out number)) {
                this.Values.Add(number);
            } else {
                this.Terms.Add(args[0]);
            }
        }

        if(2 == args.Length) // NOT
        {
            this.Type  = CommandType.Not;
            ushort number = default;
            if(ushort.TryParse(args[1], out number)) {
                this.Values.Add(number);
            } else {
                this.Terms.Add(args[1]);
            }
        }

        if(3 == args.Length) // AND, OR, LSHIFT, or RSHIFT
        {
            switch(args[1])
            {
                case "AND"   : this.Type = CommandType.And;   break;
                case "OR"    : this.Type = CommandType.Or;    break;
                case "LSHIFT": this.Type = CommandType.LShift; break;
                case "RSHIFT": this.Type = CommandType.RShift; break;
            }

            ushort number = default;
            if(ushort.TryParse(args[0], out number)) {
                this.Values.Add(number);
            } else {
                this.Terms.Add(args[0]);
            }
            if(ushort.TryParse(args[2], out number)) {
                this.Values.Add(number);
            } else {
                this.Terms.Add(args[2]);
            }
        }
    }

    public override string ToString() => this.Line;
}
