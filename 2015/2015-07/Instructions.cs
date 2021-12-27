using System.Diagnostics;
using System.IO;

class Instructions
{
    public List<Command> Commands { get; private set; }

    public Dictionary<string,Wire> Wires { get; set; }

    public Instructions()
    {
        Commands = new List<Command>();
        Wires = new Dictionary<string, Wire>();
        return;
    }

    public Instructions(string FileName) : this()
    {
        foreach(string line in File.ReadAllLines(FileName))
        {
            Command cmd = new Command(line);
            this.Commands.Add(cmd);
            this.Wires.Add(cmd.WireName, new Wire(cmd.WireName));
        }
        return;
    }

    public void ProcessCommands()
    {
        List<Command> UnprocessedCommands = this.Commands.FindAll(cmd => !cmd.Processed);

        for(int i = 0; i < UnprocessedCommands.Count; i++)
        {
            Command cmd = UnprocessedCommands[i];
            Debug.Print($"Processing command: {cmd}");
            ushort result    = default;
            ushort[] numbers = new ushort[2];
            try {
                numbers = GetNumbers(cmd);

                switch (cmd.Type)
                {
                    case CommandType.Signal:
                        result = numbers[0];
                        break;

                    case CommandType.Not:
                        result = (ushort)(~numbers[0]);
                        break;

                    case CommandType.And:
                        result = (ushort)(numbers[0] & numbers[1]);
                        break;

                    case CommandType.Or:
                        result = (ushort)(numbers[0] | numbers[1]);
                        break;

                    case CommandType.LShift:
                        result = (ushort)(numbers[0] << numbers[1]);
                        break;

                    case CommandType.RShift:
                        result = (ushort)(numbers[0] >> numbers[1]);
                        break;
                }
                this.Wires[cmd.WireName].Set(result);
                cmd.Processed = true;
            }
            catch {
                // If a wire value has not yet been set, we'll skip the current command.
            }
        }
        return;
    }

    private ushort[] GetNumbers(Command Command)
    {
        ushort[] numbers = new ushort[2];
        switch(Command.Type)
        {
            case CommandType.Signal:
            case CommandType.Not:
                if(Command.Values.Count > 0) {
                    numbers[0] = Command.Values[0];
                } else {
                    if(this.Wires[Command.Terms[0]].HasValue) {
                        numbers[0] = this.Wires[Command.Terms[0]].Value;
                    } else {
                        throw new System.Exception("Wire value not yet set.");
                    }
                }
                break;

            case CommandType.And:
            case CommandType.Or:
            case CommandType.LShift:
            case CommandType.RShift:
                if(Command.Values.Count == 0)
                {
                    if(this.Wires[Command.Terms[0]].HasValue) {
                        numbers[0] = this.Wires[Command.Terms[0]].Value;
                    } else {
                        throw new System.Exception("Wire value not yet set.");
                    }
                    if(this.Wires[Command.Terms[1]].HasValue) {
                        numbers[1] = this.Wires[Command.Terms[1]].Value;
                    } else {
                        throw new System.Exception("Wire value not yet set.");
                    }
                }
                else
                {
                    if(Command.Values.Count > 0)
                    {
                        if(this.Wires[Command.Terms[0]].HasValue) {
                            numbers[0] = this.Wires[Command.Terms[0]].Value;
                        } else {
                            throw new System.Exception("Wire value not yet set.");
                        }
                        numbers[1] = Command.Values[0];
                    }
                    else
                    {
                        numbers[0] = Command.Values[0];
                        numbers[1] = Command.Values[1];
                    }
                }
                break;
        }
        return numbers;
    }

    public bool HasUnprocessedCommands() => this.Commands.FindAll(cmd => !cmd.Processed).Count > 0;
}
