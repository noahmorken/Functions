def make_shirt(size='large', text='I love Python'):
    """Display information for a T-shirt."""
    print(f"\nI want a {size} size T-shirt.")
    print(f"I want \"{text}\" to be printed on it.")

make_shirt()
make_shirt('medium', 'MSF')
make_shirt(text='Diamond Dogs', size='small')