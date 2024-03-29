# TODO
# - pass CC, currently broken and can't handle multiword CC
Summary:	IComplete - A code completion system
Summary(pl.UTF-8):	IComplete - system dopełniania kodu
Name:		icomplete
Version:	0.4
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/icomplete/%{name}-%{version}.tar.bz2
# Source0-md5:	b802fc7c9a8a86b5dc5adf3fc62c010f
URL:		http://stud4.tuwien.ac.at/~e0125672/icomplete/
Requires:	ctags
Requires:	vim-rt >= 4:7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IComplete is a command line program, which lists possible completions
for a certain position in a source code, reusing the excellent
Exuberant-ctags program.

Features:
- Automatic generation of a tags file for the current source file by
  building a tree of included files.
- Listing members (also inherited ones) of a class; For QString s; s.
  only non-static members are suggested, for QString:: only static ones.
- Listing all function signatures of overloading methods
- Recognizes return values of methods. QWidget w; w.rect().topLeft().
  // List completions for a QPoint
- Uses the scope of the cursor position; Recognizes, if you are inside
  a method-definition and completes also private or protected variables
  for this class. For a global scope, only public members are suggested.
- Works in both console and graphical vim
- Uses a cache system for increased speed.

%description -l pl.UTF-8
IComplete to działający z linii poleceń program wypisujący możliwe
dopełnienia dla różnych fragmentów kodu źródłowego z wykorzystaniem
świetlego programu Exuberant-ctags.

Możliwości:
- Automatyczne generowanie pliku tags dla bieżącego pliku źródłowego
  poprzez budowanie drzewa włączanych plików.
- Wypisywanie składowych (także dziedziczonych) klasy; dla QString s;
  s. sugerowane są tylko niestatyczne składowe, dla QString:: tylko
  statyczne.
- Wypisywanie wszystkich sygnatur funkcji przeciążonych metod.
- Rozpoznawanie wartości zwracanych przez metody; QWidget w;
  w.rect().topLeft(). wypisze dopełnienia dla QPoint.
- Wykorzystywanie kontekstu położenia kursora; program rozpoznaje
  pozycję wewnątrz definicji metody i dopełnia także prywatne i
  chronione zmienne dla danej klasy. W kontekście globalnym sugerowane
  są wyłącznie publiczne składowe.
- Działa zarówno w terminalowym jak i graficznym vimie.
- Wykorzystuje system pamięci podręcznej dla zwiększenia prędkości
  działania.

%prep
%setup -q

%build
# not autoconf generated configure
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
./configure \
	--prefix=%{_prefix} \
	--exec-prefix=%{_exec_prefix} \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--sysconfdir=%{_sysconfdir} \
	--datadir=%{_datadir} \
	--includedir=%{_includedir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--localstatedir=%{_localstatedir} \
	--sharedstatedir=%{_sharedstatedir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/icomplete
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/icomplete.conf
%{_datadir}/vim/vimfiles/autoload/cppcomplete.vim
%{_datadir}/vim/vimfiles/plugin/icomplete.vim
