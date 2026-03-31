subroutine compute_mean(grid, nx, ny, nz, mean_val)
    implicit none
    
    ! 1. Variable Declarations
    integer, intent(in) :: nx, ny, nz
    real(8), intent(in) :: grid(nx, ny, nz)
    real(8), intent(out) :: mean_val
    
    ! 2. f2py Directives (The "Magic")
    ! Tell f2py that Python only needs to pass 'grid'. 
    ! It will automatically calculate nx, ny, nz using NumPy's shape() function!
    !f2py intent(in) :: grid
    !f2py intent(hide), depend(grid) :: nx = shape(grid,0), ny = shape(grid,1), nz = shape(grid,2)
    !f2py intent(out) :: mean_val

    ! Local variables
    integer :: i, j, k
    real(8) :: total_sum, total_elements

    total_sum = 0.0d0
    total_elements = dble(nx) * dble(ny) * dble(nz)

    if (total_elements == 0.0d0) then
        mean_val = 0.0d0
        return
    end if

    ! 3. The Math Loop
    ! CRITICAL: Fortran is Column-Major! The innermost loop MUST be the first dimension (i)
    do k = 1, nz
        do j = 1, ny
            do i = 1, nx
                total_sum = total_sum + grid(i, j, k)
            end do
        end do
    end do

    mean_val = total_sum / total_elements

end subroutine compute_mean

