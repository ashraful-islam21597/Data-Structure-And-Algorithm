class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children = []
        self.parent =  None
    def add_child(self,child):
        child.parent= self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_tree(self):

        spaces= " "*self.get_level()*5
        prefix = spaces+ "|__" if self.parent else " "
        print(prefix,self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree():
    root=TreeNode("Alphabet")

    vowel=TreeNode("Vowel")
    vowel.add_child(TreeNode("A"))
    vowel.add_child(TreeNode("E"))
    vowel.add_child(TreeNode("I"))
    vowel.add_child(TreeNode("O"))
    vowel.add_child(TreeNode("U"))

    consonant=TreeNode("Consonant")
    consonant.add_child(TreeNode("B"))
    consonant.add_child(TreeNode("C"))
    consonant.add_child(TreeNode("D"))
    consonant.add_child(TreeNode("F"))
    consonant.add_child(TreeNode("G"))

    root.add_child(vowel)
    root.add_child(consonant)
    return root

tree=build_tree()
tree.get_level()
tree.print_tree()

