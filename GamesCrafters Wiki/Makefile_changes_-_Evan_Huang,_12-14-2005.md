Makefile\_changes\_-\_Evan\_Huang,\_12-14-2005
==============================================

Intention to change compiler flags for all sources:
"-Wimplicit" -&gt; "-Wall" (WARNING: this will generate TONS of warnings for stale code and new code alike)
Add "-g" to core source compilation in non-cygwin environments to aid debugging.
