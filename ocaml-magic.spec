Name:     ocaml-magic

Version:  0.7.3
Release:  1
Summary:  OCaml bindings for libmagic
License:  GPLv2+
URL:      https://github.com/Chris00/ocaml-magic
Source0:  https://github.com/Chris00/ocaml-magic/archive/3b883ad9cf7c32dc1309d4200bd0af87e5841119.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: file-libs

%prep
%setup -q 

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
/usr/lib64/ocaml/magic/META
/usr/lib64/ocaml/magic/xmlplaylist.a
/usr/lib64/ocaml/magic/xmlplaylist.cma
/usr/lib64/ocaml/magic/xmlplaylist.cmi
/usr/lib64/ocaml/magic/xmlplaylist.cmxa
/usr/lib64/ocaml/magic/xmlplaylist.mli
/usr/lib64/ocaml/magic/xmlplaylist.cmx

%description
OCAML bindings for libmagic
