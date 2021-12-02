public class Coordinates
{
    public uint Position { get; }

    public uint Depth { get; }

    public uint Multiplied { get; }

    public Coordinates(uint inPosition, uint inDepth)
    {
        Position    = inPosition;
        Depth       = inDepth;
        Multiplied  = inPosition * inDepth;
    }
}