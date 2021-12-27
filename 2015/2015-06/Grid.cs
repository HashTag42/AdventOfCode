using System.Collections.Generic;

class Grid
{
    private uint size { get; init; }
    private ulong[,] grid { get; set; }

    public Grid()
    {
        this.size = 1000;
        this.grid = new ulong[this.size,this.size];
    }

    public Grid(uint Part, Instructions Instructions) : this()
    {
        foreach(Command cmd in Instructions.Commands)
        {
            this.DoCommand(Part, cmd);
        }
    }

    public void DoCommand(uint Part, Command Command)
    {
        for(int r = Command.Start.row; r <= Command.End.row; r++)
        {
            for(int c = Command.Start.col; c <= Command.End.col; c++)
            {
                switch(Command.Cmd)
                {
                    case CommandType.turnOn:
                        if(1 == Part)
                        {
                            this.grid[r,c] = 1;
                        }
                        else if(2 == Part)
                        {
                            this.grid[r,c] += 1;
                        }
                        break;

                    case CommandType.turnOff:
                        if(1 == Part)
                        {
                            this.grid[r,c] = 0;
                        }
                        else if(2 == Part)
                        {
                            this.grid[r,c] = (this.grid[r,c] > 0) ? this.grid[r,c] -= 1 : 0;
                        }
                        break;

                    case CommandType.toggle:
                        if(1 == Part)
                        {
                            this.grid[r,c] = (ulong)((0 == this.grid[r,c]) ? 1 : 0);
                        }
                        else if(2 == Part)
                        {
                            this.grid[r,c] += 2;
                        }
                        break;
                }
            }
        }
    }

    public ulong Sum()
    {
        ulong sum = 0;
        for(int r = 0; r < this.size; r++)
        {
            for(int c = 0; c < this.size; c++)
            {
                sum += this.grid[r,c];
            }
        }

        return sum;
    }

}