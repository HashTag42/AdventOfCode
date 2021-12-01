using System;

public class Package
{
    public uint Length { get; }
    public uint Width { get; }
    public  uint Height { get; }
    public uint[] Dimensions { get; }

    public Package(string textDimensions)
    {
        string[] terms = textDimensions.Split('x');

        Dimensions = new uint[3];
        Length  = Dimensions[0] = uint.Parse(terms[0]);
        Width   = Dimensions[1] = uint.Parse(terms[1]);
        Height  = Dimensions[2] = uint.Parse(terms[2]);
        Array.Sort(Dimensions);
    }
}