    def delete(self, domain, name):
        bX = self.right(self.head, domain, name, 0)
        if bX is None:
            return None

        bY = self.down(self.head, domain, name, 0)
        if bY is None:
            return None

        bX = self.down(bX.right, domain, name, 0)
        if bX is None:
            return None

        bY = self.right(bY.down, domain, name, 0)
        if bY is None:
            return None

        if bX.down.name == name and bY.right.domain == domain:
            result = bX.down
            if bX.down.back is None:
                bX.down = bX.down.down
                bY.right = bY.right.right
                self.validateHeaders(self)
                return result

            bX.down = bX.down.back
            bX.down.down = result.down
            bX.down.right = result.right
            bY.right = bX.down
            self.validateHeaders()
            return result
        else:
            bX = bX.down
            while bX.back is not None and bX.back.name != name:
                bX = bX.back

            if bX.back is None:
                return None
            else:
                result = bX.back
                bX.back = bX.back.back
                result.back = None
                self.validateHeaders()
                return result

    @staticmethod
    def validateHeaders(self):
        buffer = self.head
        while buffer.right is not None:
            if buffer.right.down is None:
                buffer.right = buffer.right.right
            buffer = buffer.right

        buffer = self.head
        while buffer.down is not None:
            if buffer.down.right is None:
                buffer.down = buffer.down.down

            buffer = buffer.down

       def login(self, enterprise, department, user, password):
        result = self.search(enterprise, department, user)
        if result is not None:
            if result.user.password == password:
                return result

        return None