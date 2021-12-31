class Route
{
    public List<Connection> ConnectionList  { get; private set; }

    public List<string>     CityList        { get; private set;}

    public int              TotalDistance   { get; private set; }

    public Route()
    {
        this.ConnectionList = new List<Connection>();
        this.CityList       = new List<string>();
        this.TotalDistance  = 0;
    }

    public bool TryAdd(Connection newConnection)
    {
        bool added = false;

        if(     (0 == this.ConnectionList.Count)
            || ((!this.ConnectionList.Contains(newConnection)
            &&  (this.ConnectionList[this.ConnectionList.Count - 1].CityB == newConnection.CityA)))
          )
        {
            this.ConnectionList.Add(newConnection);
            this.TotalDistance += newConnection.Distance;
            added = true;
        }

        return added;
    }

    public bool TryAdd(string CityA, string CityB, int Distance)
    {
        Connection newConnection = new Connection(CityA, CityB, Distance);
        return this.TryAdd(newConnection);
    }

    public bool TryAdd(string City, int Distance)
    {
        bool added = false;
        if(!this.CityList.Contains(City))
        {
            this.CityList.Add(City);
            this.TotalDistance += Distance;
            added = true;
        }
        return added;
    }

    public override string ToString()
    {
        string output = "";
        int c = 0;
        for(; c < this.ConnectionList.Count; c++)
        {
            output += this.ConnectionList[c].CityA + " -> ";
            if(c == this.ConnectionList.Count -1 )
            {
                output += this.ConnectionList[c].CityB;
            }
        }
        output += " = " + this.TotalDistance;
        return output;
    }
}
