class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for a in asteroids:
            # If asteroid move the right, append to stack
            if a >= 0:
                st.append(a)
            # If asteroid move to the left, it might collided when there is asteroid moving to the right
            else:
                # check, as long as
                # 1. there is asteroid (while st) and
                # 2. it is moving to the right and
                # 3. the asteroid moving to the right is smaller than the asteroid moving to the left
                # 4. implicitly if the asteroid moving to the left is smaller, destroy the asteroid moving to the left (not adding to stack)
                # then:
                # blass of the asteroid moving to the right (st.pop())
                while st and st[-1] > 0 and st[-1] < abs(a):
                    st.pop()
                # if no asteroid moving to the right (not st) or if the previous asteroid is also moving to the left, append the current asteroid
                if not st or st[-1] < 0:
                    st.append(a)
                # if asteroid moving to the left and asteroid moving to the right are the same
                # destroy both ()
                elif st[-1] == abs(a):
                    st.pop()
        return st