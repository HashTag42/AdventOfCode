class Grid
{
    private int size { get; init; }
    private int[,] grid { get; set; }


    public Grid()
    {
        this.size = 1000;
        this.grid = new int[this.size,this.size];
    }

    public void Action(Command Command)
    {
        for(int r = Command.Start.row; r <= Command.End.row; r++)
        {
            for(int c = Command.Start.col; c <= Command.End.col; c++)
            {
                switch(Command.Cmd)
                {
                    case CommandType.turnOn:
                        this.grid[r,c] = 1;
                        break;
                    case CommandType.turnOff:
                        this.grid[r,c] = 0;
                        break;
                    case CommandType.toggle:
                        this.grid[r,c] = this.grid[r,c] == 0 ? 1 : 0;
                        break;
                }
            }
        }

    }

    public int Sum()
    {
        int sum = 0;
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