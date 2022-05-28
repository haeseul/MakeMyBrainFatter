# Python을 사용하여 다음 지침에 따라 라이브러리(TENSORFLOW, NUMPY, OR SCIPY)를 가져오지 않고 클래스를 구성하시오
# - data와 shape이 주어지면 중첩 list을 사용하여 텐서 함수를 구성
# - 텐서는 n차원 행렬 (행렬 순서는 스칼라, 벡터, 행렬, 텐서)
# - data[] : 모든 숫자(int 또는 float), 길이 제한X
# - shape[]: 양의 정수 -> shape이 empty list면 [] 출력, 길이 제한X
# - 구성된 텐서는 인스턴스 변수로 저장하거나 표준 출력으로 인쇄하거나 둘 다
# - 데이터 넘치면 자르기, 남으면 0으로 채우기



class Tensor():
    def __init__ (self, data, shape):
        self.data = data
        self.shape = shape
        self.tensor = Tensor.shape_data(self)

    def shape_data(self):
      m = 0
      if self.shape == []:
        return []

      ## Tensor
      elif len(self.shape) == 3:
        self.tensor = [[[0 for k in range(self.shape[2])] for j in range(self.shape[1])] for i in range(self.shape[0])]
        for i in range(len(self.tensor)):
          for j in range(len(self.tensor[i])):
            for k in range(len(self.tensor[i][j])):
              if m >= len(self.data):
                return self.tensor
              else:
                self.tensor[i][j][k] = self.data[m]
                m += 1
        return self.tensor

      ## Matrix
      elif len(self.shape) == 2:
        self.tensor = [[0 for k in range(self.shape[1])] for j in range(self.shape[0])]
        for i in range(len(self.tensor)):
          for j in range(len(self.tensor[i])):
            if m >= len(self.data):
              return self.tensor
            else:
              self.tensor[i][j] = self.data[m]
              m += 1
        return self.tensor

      elif len(self.shape) == 1:
        ## Vector
        if self.shape != [1]:
          self.tensor = [0 for k in range(self.shape[0])]
          for i in range(len(self.tensor)):
            if m >= len(self.data):
              return self.tensor
            else:
              self.tensor[i] = self.data[m]
              m += 1
          return self.tensor

        ## Scalar
        else:
          if self.data == []:
            return 0
          else:
            return self.data[0]

    # 텐서는 3차원 이상의 n-dimensional한 자료구조이다. 쉐입이 3개 이상 나올 수 있음
    # 다시 시도!
      else:
        raise ValueError



# >>> data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
# >>> shape0 = [2, 3, 2]
# >>> tensor0 = Tensor(data0, shape0)

# output:
# [[[0, 1], [2, 3], [4, 5]], [[0.1, 0.2], [-3, 0], [0, 0]]]


# >>> data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]
# >>> shape1 = [5, 2]
# >>> tensor1 = Tensor(data1, shape1)

# output:
# [[0, 1], [2, 3], [4, 5], [0.1, 0.2], [-3, -2]]



# data0 = []
# data1 = [8]
# data14 = [100, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]

# shape_tensor = [4, 2, 3]
# shape_matrix = [3, 5]
# shape_vector = [4]
# shape_scalar = [1]
# shape_empty = []
# shape_over = [5, 4, 3, 2]

# T = Tensor(data1, [2,3,4,5])
# T.tensor