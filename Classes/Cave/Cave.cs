using System;   // IEquatable

class Cave: IEquatable<Cave>
{
    public enum CaveSize { Big, Small }

    public string Name { get; init; }

    public CaveSize Size { get; init; }

    public Cave(string Name)
    {
        this.Name= Name;
        this.Size= (this.Name == this.Name.ToUpper()) ? CaveSize.Big : CaveSize.Small;
    }

    public override bool Equals(object Object)
    {
        bool isEqual= false;

        if(Object != null && Object is Cave)
        {
            isEqual= Equals(Object);
        }

        return isEqual;
    }

    public bool Equals(Cave Other)
    {
        bool isEqual= false;

        if(Other != null && this.Name == Other.Name)
        {
            isEqual= true;
        }

        return isEqual;
    }

    public override int GetHashCode()
    {
        return this.Name.GetHashCode();
    }

    public override string ToString()
    {
        return (this.Name + ":" + this.Size);
    }

}
