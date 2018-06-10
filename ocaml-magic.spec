%define debug_package %{nil}

Name:     ocaml-magic
Version:  0.7.3
Release:  3
Summary:  OCaml bindings for libmagic

%define git_ish 3b883ad9cf7c32dc1309d4200bd0af87e5841119
%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:  GPLv2+
URL:      https://github.com/Chris00/ocaml-magic
Source0:  https://github.com/Chris00/ocaml-magic/archive/%{git_ish}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: file-devel
BuildRequires: which
Requires:      file


%description
OCAML bindings for libmagic


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{git_ish}

%build
%configure \
   --prefix=%{_prefix} \
   --disable-ldconf \
make byte
make opt

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
%doc README.md
%license LICENSE
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license LICENSE
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Sun Dec  9 2018 Lucas Bickel <hairmare@rabe.ch> - 0.7.3-2
- Initialize RPM changelog
- Cleanup and add separate -devel subpackage
- Remove legacy old-school optional opt build
