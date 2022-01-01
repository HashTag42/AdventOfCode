/// Supports a list of unique items.
class UniqueList<T> : List<T>
{
    /// Adds an item to the list only if it's not yet contained in the list.
    public void AddIfNew(T Obj)
    {
        // Objects are only added to the list once.
        if(false == base.Contains(Obj))
        {
            base.Add(Obj);
        }
        return;
    }
}