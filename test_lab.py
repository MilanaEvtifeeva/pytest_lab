#Eвтифеева Милана 107б
import pytest
from lab import *

def test_multiply():
    assert  multiply(1,1)==1
    assert multiply(-6,2) == -12
    assert multiply(-5,-5) ==25
    assert multiply(0,4) == 0
    assert multiply(7,0) == 0

def test_divide():
    assert divide(1,1)==1
    assert divide(-6,2) ==-3
    assert divide(-45,-5) == 9
    assert divide(0,4) ==0
    assert divide(7,0) == "Делить на  0  нельзя"

def test_point_distance():
    assert point_distance(1,1,1,1)==0
    assert point_distance(-2,-4,3,8) == 13
    assert point_distance(0,0,0,10) == 10
    assert point_distance(1,2,4,6) == 5
    assert point_distance(0,0,3,4) == 5

def test_quad():
    assert quad(1,-3,2)==(1,2)
    assert quad(1,-5,6) == (2,3)
    assert quad(1,2,1) == -1
    assert quad(1,0,1) == ("Дискриминант меньше нуля. Корней нет")
    assert quad(0,2,-4) == 2

def test_geom_sum():
    assert geom_sum(2,3,3)==26
    assert geom_sum(1,2,5) == 31
    assert geom_sum(5,2,1) == 5
    assert geom_sum(3,2,5) == 93
    assert geom_sum(4,-1,4) == 0

