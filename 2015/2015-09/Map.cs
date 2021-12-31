using System;
using System.Diagnostics;

class Map
{
    public int ShortestDistance { get; private set; }

    private List<Connection> Connections { get; init; }

    private List<string> Cities { get; init; }

    private int[,] DistanceTable { get; set; }

    public Map()
    {
        this.Connections      = new List<Connection>();
        this.Cities           = new List<string>();
        this.DistanceTable    = new int[0,0];
        this.ShortestDistance = int.MaxValue;
    }

    public Map(string FilePath) : this()
    {
        this.LoadMap(FilePath);
        this.BuildMatrix();
        this.FindRoutes();
    }

    /// Builds a map based on the data read from the input file.
    private void LoadMap(string FilePath)
    {
        foreach(string line in File.ReadAllLines(FilePath))
        {
            Connection connection = new Connection(line);
            this.Connections.Add(connection);
            // Cities are only added once to the list.
            if(!this.Cities.Contains(connection.CityA)) { this.Cities.Add(connection.CityA); }
            if(!this.Cities.Contains(connection.CityB)) { this.Cities.Add(connection.CityB); }
        }
    }

    /// This method builds a weighted adjacency matrix stored in a 2-dimentional array.
    /// Each cell stores the distance between the cities.
    private void BuildMatrix()
    {
        int size = this.Cities.Count;
        this.DistanceTable = new int[size, size];

        this.Cities.Sort(); // This is optional.

        foreach(Connection connection in this.Connections)
        {
            int row = this.Cities.IndexOf(connection.CityA);
            int col = this.Cities.IndexOf(connection.CityB);
            this.DistanceTable[row,col] = this.DistanceTable[col,row] = connection.Distance;
        }
    }

    /// This method finds all possible routes, adds-up the total distance of each route, and identifies the shortest one.
    private void FindRoutes()
    {
        int size = this.Cities.Count;
        int[] values = new int[size];
        for(int i = 0; i < size; i++) { values[i] = i; }

        int count = 0;
        foreach (IEnumerable<int> route in values.GetPermutations())
        {
            count++;

            int[] numbers = new int[size];
            int index = 0;
            foreach(int p in route)
            {
                numbers[index] = p;
                index++;
            }

            // Adds-up the distances between each city in the route.
            int distance = 0;
            for(int i = 0; i < values.Length - 1; i++)
            {
                int row = numbers[i];
                int col = numbers[i+1];
                distance += this.DistanceTable[row,col];
            }
            Debug.Write($"{count}: {string.Join(" -> ", route)} = {distance}" );

            //
            if(distance < this.ShortestDistance)
            {
                this.ShortestDistance = distance;
                Debug.Write("\t New minimum distance!");
            }
            Debug.Write(Environment.NewLine);
        }
    }

    public override string ToString()
    {
        string output = "";
        string separator = ",";
        int size = this.Cities.Count;

        output = "Cities," + String.Join(separator, this.Cities) + Environment.NewLine;

        for(int row = 0; row < size; row++)
        {
            output += this.Cities[row] + separator;
            for(int col = 0; col < size; col++)
            {
                output += this.DistanceTable[row,col] + separator;
            }
            output  = output.Remove(output.Length - separator.Length, separator.Length)
                    + Environment.NewLine;
        }

        return output;
    }

}
