import threading
import ipdb as pdb


class Thread(threading.Thread):
  def run(self):
    a_variable = 1
    print(a_variable)
    pdb.set_trace()
    return


if __name__ == '__main__':
    pdb.set_trace()
    Thread().start()
    print('Done')
