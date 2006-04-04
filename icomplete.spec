#
Summary:	IComplete - A code completion system
Name:		icomplete
Version:	0.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/icomplete/%{name}-%{version}.tar.bz2
# Source0-md5:	cc2ca34af559f9face1e0670c0b0d61b
URL:		http://stud4.tuwien.ac.at/~e0125672/icomplete
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
- Listing members (also inherited ones) of a class For QString s; s.
  only non-static members are suggested, for QString:: only static ones.
- Listing all function signatures of overloading methods
- Recognizes return values of methods. QWidget w; w.rect().topLeft().
  // List completions for a QPoint
- Uses the scope of the cursor position Recognizes, if you are inside
  a method-definition and completes also private or protected variables
  for this class. For a global scope, only public members are suggested.
- Works in both console and graphical vim
- Uses a cache system for increased speed.

%prep
%setup -q

%build
%configure
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
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/icomplete.conf
%{_datadir}/vim/vimfiles/autoload/cppcomplete.vim
%{_datadir}/vim/vimfiles/plugin/icomplete.vim
