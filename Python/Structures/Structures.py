import subprocess


class Asset(object):
    def __init__(self, id=None, name=None, desc=None):
        self.id = id
        self.name = name
        self.desc = desc

    def __str__(self):
        return str(self.id) + ", " + str(self.name) + ", " + str(self.desc) + ";"


class TreeNode(object):
    def __init__(self, asset=None, left=None, right=None):
        self.asset = asset
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.asset)


class AVLTree(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, id, name, desc):
        node = TreeNode(Asset(id, name, desc))
        if self.head is None:
            self.head = node
            return node
        else:
            result = self.insertNode(self.head, node)
            self.head = AVLTree.balance(self.head)
            return result

    def search(self, id):
        node = AVLTree.get(self.head, id)
        if node is None:
            return None
        elif node.asset.id == id:
            return node
        elif node.asset.id > id:
            return node.left
        else:
            return node.right

    def delete(self, id):
        node = AVLTree.get(self.head, id)

        if node == self.head and self.head.asset.id == id:
            buffer = AVLTree.getRight(self.head.left)
            self.head = buffer.right
            buffer.right = None
            buffer = AVLTree.getLeft(self.head)
            if buffer.left is None:
                buffer.left = node.left
            else:
                buffer.left.left = node.left

            self.head.right = node.right
            node.left = None
            node.right = None
            self.head = AVLTree.balance(self.head)
            return node

        if node.left.asset.id == id:
            result = node.left
            node.left = result.right
            buffer = AVLTree.getLeft(result.left)
            if buffer.left is None:
                buffer.left = node.left
            else:
                buffer.left.left = node.left

            result.left = None
            result.right = None
            self.head = AVLTree.balance(self.head)
            return result
        else:
            result = node.right
            node.right = result.right
            buffer = AVLTree.getLeft(result.right)
            if buffer.left is None:
                buffer.left = node.left
            else:
                buffer.left.left = node.left

            result.left = None
            result.right = None
            self.head = AVLTree.balance(self.head)
            return result

    def traversal(self, mode=0):
        if mode == 0:
            return AVLTree.inorder(self.head)

    @staticmethod
    def preorder(node):
        result = str(node) + "\n"
        if node.left is not None:
            result += AVLTree.preorder(node.left)
        if node.right is not None:
            result += AVLTree.preorder(node.right)
        return result

    @staticmethod
    def inorder(node):
        result = ""
        if node is None:
            return ""
        if node.left is not None:
            result += AVLTree.inorder(node.left)
        result += str(node) + "\n"
        if node.right is not None:
            result += AVLTree.inorder(node.right)
        return result

    @staticmethod
    def postorder(node):
        result = ""
        if node.left is not None:
            result += AVLTree.postorder(node.left)
        if node.right is not None:
            result += AVLTree.postorder(node.right)
        result += str(node) + "\n"
        return result

    @staticmethod
    def insertNode(ref, node):
        if ref.asset.id > node.asset.id:
            if ref.left is None:
                ref.left = node
                return node
            else:
                return AVLTree.insertNode(ref.left, node)
        elif ref.asset.id < node.asset.id:
            if ref.right is None:
                ref.right = node
                return node
            else:
                return AVLTree.insertNode(ref.right, node)

    @staticmethod
    def balance(node):
        if node.left is not None:
            node.left = AVLTree.balance(node.left)

        if node.right is not None:
            node.right = AVLTree.balance(node.right)

        ef = AVLTree.depth(node.right) - AVLTree.depth(node.left)
        if ef == 2:
            ef = AVLTree.depth(node.right.right) - AVLTree.depth(node.right.left)
            if ef == 1:
                return AVLTree.right(node)
            elif ef == -1:
                node.right = AVLTree.left(node.right)
                return AVLTree.right(node)

        elif ef == -2:
            ef = AVLTree.depth(node.left.right) - AVLTree.depth(node.left.left)
            if ef == -1:
                return AVLTree.left(node)
            elif ef == 1:
                node.left = AVLTree.right(node.right)
                return AVLTree.left(node)
        else:
            return node

    @staticmethod
    def left(node):
        result = node.left
        buffer = result.right
        result.right = node
        result.right.left = buffer
        return result

    @staticmethod
    def right(node):
        result = node.right
        buffer = result.left
        result.left = node
        result.left.right = buffer
        return result

    @staticmethod
    def getLeft(node):
        if node.left is None:
            return node
        elif node.left.left is None:
            return node
        else:
            return AVLTree.getPre(node.left)

    @staticmethod
    def getRight(node):
        if node.right is None:
            return node
        elif node.right.right is None:
            return node
        else:
            return AVLTree.getPre(node.right)

    @staticmethod
    def get(ref, id):
        if ref.asset.id == id:
            return ref

        if ref.left is not None and ref.asset.id > id:
            if ref.left.asset.id == id:
                return ref

            return AVLTree.get(ref.left, id)
        elif ref.right is not None and ref.asset.id < id:
            if ref.right.asset.id == id:
                return ref

            return AVLTree.get(ref.right, id)
        else:
            return None

    @staticmethod
    def depth(node):
        if node is None:
            return 1

        left = abs(AVLTree.depth(node.left))
        right = abs(AVLTree.depth(node.right))

        return (left + 1, right + 1)[left < right]


class User(object):
    def __init__(self, user=None, name=None, password=None):
        self.user = user
        self.name = name
        self.password = password


class MatrixNode(object):
    def __init__(self, enterprise=None, department=None, user=None, right=None, down=None, back=None):
        self.enterprise = enterprise
        self.department = department
        self.user = user
        self.right = right
        self.down = down
        self.back = back
        self.tree = AVLTree()

    def __str__(self):
        if self.user is not None:
            return str(self.user.user + ", " + self.user.name + ", " + self.enterprise + ", " + self.department + ":")
        else:
            return str(self.enterprise + ", " + self.department + ";")


class SparseMatrix(object):
    def __init__(self):
        self.head = MatrixNode("ENC", "ENC")

    def insert(self, enterprise, department, user, name, password):
        body = User(user, name, password)
        bX = self.right(self.head, enterprise, "ENC")
        bY = self.down(self.head, "ENC", department)
        bX = self.down(bX.right, enterprise, department, body)
        bY = self.right(bY.down, enterprise, department, body)
        if bX.down == bY.right and bX.down.user.user == user:
            return None

        bX.down.right = bY.right.right
        bY.right = bX.down
        if bX.down.enterprise == enterprise and bX.down.department == department and bX.down.user.user == user:
            return bX.down

        result = self.back(bX.down, enterprise, department, body)
        return result

    def search(self, enterprise, department, user):
        bX = self.right(self.head, enterprise, department, mode=0)
        if bX is None:
            return None

        bY = self.down(self.head, enterprise, department, mode=0)
        if bY is None:
            return None

        bX = self.down(bX.right, enterprise, department, mode=0)
        if bX is None:
            return None

        bY = self.right(bY.down, enterprise, department, mode=0)
        if bY is None:
            return None

        if bX.down.department == department and bY.right.enterprise == enterprise:
            result = bX.down
            if result.user.user == user:
                return result
            else:
                while result.back is not None and result.back.user.user != user:
                    result = result.back

                return result.back

        else:
            return None

    @staticmethod
    def right(node, enterprise, department, body=None, mode=1):
        if mode == 1:
            if node.enterprise > enterprise and node.enterprise != "ENC":
                temp = node
                node = MatrixNode(enterprise, department, body)
                node.right = temp
                return node

            buffer = node
            while buffer.right is not None and buffer.right.enterprise < enterprise:
                buffer = buffer.right

            if buffer.right is None:
                buffer.right = MatrixNode(enterprise, department, body)
            elif buffer.right.enterprise > enterprise:
                temp = buffer.right
                buffer.right = MatrixNode(enterprise, department, body)
                buffer.right.right = temp

            return buffer
        else:
            if node.enterprise > enterprise and node.enterprise != "ENC":
                return None

            buffer = node
            while buffer.right is not None and buffer.right.enterprise < enterprise:
                buffer = buffer.right

            if buffer.right is None or buffer.right.enterprise > enterprise:
                return None

            return buffer

    @staticmethod
    def down(node, enterprise, department, body=None, mode=1):
        if mode == 1:
            if node.department > department and node.department != "ENC":
                temp = node
                node = MatrixNode(enterprise, department, body)
                node.down = temp
                return node

            buffer = node
            while buffer.down is not None and buffer.down.department < department:
                buffer = buffer.down

            if buffer.down is None:
                buffer.down = MatrixNode(enterprise, department, body)
            elif buffer.down.department > department:
                temp = buffer.down
                buffer.down = MatrixNode(enterprise, department, body)
                buffer.down.down = temp

            return buffer
        else:
            if node.department > department and node.department != "ENC":
                return None

            buffer = node
            while buffer.down is not None and buffer.down.department < department:
                buffer = buffer.down

            if buffer.down is None or buffer.down.department > department:
                return None

            return buffer

    @staticmethod
    def back(node, enterprise, department, body):
        if node.enterprise == enterprise and node.department == department and node.user.user == body.user:
            return None
        buffer = node

        while buffer.back is not None:
            if buffer.back.user.user == body.user:
                return None
            buffer = buffer.back

        buffer.back = MatrixNode(enterprise, department, body)
        return buffer.back

    def reportMatrix(self):
        buffer = self.head
        x = 0
        y = 0
        report = open('MatrixReport.dot', 'w+')
        report.write(
            "digraph SparseMatrix{\n\t")
        while buffer is not None:
            buffer2 = buffer
            x += 1
            while buffer2 is not None:
                y += 1
                if buffer2.right is not None:
                    report.write("\n\t\"" + str(buffer2) + "\"->\"" + str(buffer2.right) + "\"")

                if buffer2.down is not None:
                    report.write("\n\t\"" + str(buffer2) + "\"->\"" + str(buffer2.down) + "\"")

                report.write("\n\t\"" + str(buffer2) + "\"[label=\"" + str(buffer2) + "\" shape=\"square\" ]")

                buffer2 = buffer2.down

            buffer = buffer.right

        report.write("}")
        report.close()
        gen = open('gen.sh', 'w+')
        gen.write("dot MatrixReport.dot -Tjpg -o Matrix.jpg\n")
        gen.write("xdg-open Matrix.jpg\n")
        gen.close()
        subprocess.call(['./gen.sh'], shell=True)

    def report(self, domain, name):
        bX = self.right(self.head, domain, name, 0)
        bY = self.down(self.head, domain, name, 0)
        bX = self.down(bX.right, domain, name, 0)
        bY = self.right(bY.down, domain, name, 0)
        if bX.down.name == name and bY.right.domain == domain:
            buffer = bX.down
            i = 0
            report = open('MatrixNodeReport.dot', 'w+')
            report.write("digraph MatrixNode{\n\t" + str(i) + "[label=\"" + str(buffer) + "\"]\n")
            while buffer.back is not None:
                report.write("\t" + str(i + 1) + "[label=\"" + str(buffer.back) + "\"]\n")
                report.write("\t" + str(i) + "->" + str(i + 1) + "\n")
                buffer = buffer.back
                i += 1

            report.write("}")
            report.close()
            gen = open('gen.sh', 'w+')
            gen.write("dot MatrixNodeReport.dot -Tjpg -o MatrixNode.jpg\n")
            gen.write("xdg-open MatrixNode.jpg\n")
            gen.close()
            subprocess.call(['./gen.sh'], shell=True)
        else:
            bX = bX.down
            while bX.back is not None and bX.back.name != name:
                bX = bX.back

            if bX.back is None:
                return None
            else:
                buffer = bX.back
                i = 0
                report = open('MatrixNodeReport.dot', 'w+')
                report.write("digraph MatrixNode{\n\t" + str(i) + "[label=\"" + str(buffer) + "\"]\n")
                while buffer.back is not None:
                    report.write("\t" + str(i + 1) + "[label=\"" + str(buffer.back) + "\"]\n")
                    report.write("\t" + str(i) + "->" + str(i + 1) + "\n")
                    buffer = buffer.back
                    i += 1

                report.write("}")
                report.close()
                gen = open('gen.sh', 'w+')
                gen.write("dot MatrixNodeReport.dot -Tjpg -o MatrixNode.jpg\n")
                gen.write("xdg-open MatrixNodeReport.jpg\n")
                gen.close()
                subprocess.call(['./gen.sh'], shell=True)
                return

