include config.mk

MAKE=make

prefix ?= /usr/local

builddir=build/out
abs_builddir := $(abspath $(builddir))
hdir=$(abspath ./)

all: config.mk
	$(MAKE) -C "./build" builddir="$(abs_builddir)"

binaries=$(prefix)/lib/libgypaes.a
headers=$(prefix)/include/aes.h $(prefix)/include/brg_types.h

$(binaries): $(prefix)/lib/%: $(builddir)/obj.target/%
	cp $< $@

$(headers): $(prefix)/include/%: $(hdir)/%
	cp $< $@


install: $(binaries) $(headers) 

#$(directories)

# $(directories), uninstall, clean, .PHONY, etc.
