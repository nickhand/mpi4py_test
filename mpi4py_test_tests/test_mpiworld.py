from mpi4py_test.mpi import MPITest

@MPITest(commsize=[1, 2])
def test_mpicomm(comm):
    assert comm is not None

from mpi4py_test.mpi import MPIWorld
# this is deprecated
@MPIWorld(NTask=[1, 2], required=(1, 2))
def test_mpiworld(comm):
    assert comm is not None
