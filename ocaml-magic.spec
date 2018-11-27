Name:     ocaml-magic

%define git_ish 3b883ad9cf7c32dc1309d4200bd0af87e5841119

Version:  0.7.3
Release:  2
Summary:  OCaml bindings for libmagic
License:  GPLv2+
URL:      https://github.com/Chris00/ocaml-magic
Source0:  https://github.com/Chris00/ocaml-magic/archive/%{git_ish}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: file-devel
Requires:      file

%prep
%setup -q -n ocaml-magic-%{git_ish}

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
%{_libdir}/ocaml/magic/
%{_libdir}/ocaml/magic/META
%{_libdir}/ocaml/magic/magic.a
%{_libdir}/ocaml/magic/magic.cma
%{_libdir}/ocaml/magic/magic.cmi
%{_libdir}/ocaml/magic/magic.cmxa
%{_libdir}/ocaml/magic/magic.mli
%{_libdir}/ocaml/magic/magic.cmx
%{_libdir}/ocaml/magic/libmagic_stubs.a
%{_libdir}/ocaml/stublibs/dllmagic_stubs.so
%{_libdir}/ocaml/stublibs/dllmagic_stubs.so.owner

%description
OCAML bindings for libmagic
