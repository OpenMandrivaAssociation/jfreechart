
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		jfreechart
Version:	1.0.14
Release:	10.0
License:	GPLv3+
Source0:	jfreechart-1.0.14-10.0-omv2014.0.noarch.rpm
Source1:	jfreechart-swt-1.0.14-10.0-omv2014.0.noarch.rpm
Source2:	jfreechart-javadoc-1.0.14-10.0-omv2014.0.noarch.rpm

URL:		https://abf.rosalinux.ru/openmandriva/jfreechart
BuildArch:	noarch
Summary:	jfreechart bootstrap version
Requires:	javapackages-bootstrap
Requires:	java
Requires:	jcommon >= 1.0.17
Requires:	jpackage-utils
Requires:	servlet
Provides:	jfreechart = 1.0.14-10.0:2014.0
Provides:	mvn(org.jfree:jfreechart) = 1.0.14
Provides:	osgi(org.jfree.jfreechart) = 1.0.14

%description
jfreechart bootstrap version.

%files
/usr/share/doc/jfreechart
/usr/share/doc/jfreechart/ChangeLog
/usr/share/doc/jfreechart/NEWS
/usr/share/doc/jfreechart/README.txt
/usr/share/doc/jfreechart/licence-LGPL.txt
/usr/share/java/jfreechart
/usr/share/java/jfreechart/jfreechart.jar
/usr/share/maven-fragments/jfreechart
/usr/share/maven-poms/JPP.jfreechart-jfreechart.pom

#------------------------------------------------------------------------
%package	-n jfreechart-swt
Version:	1.0.14
Release:	10.0
Summary:	jfreechart-swt bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-swt
Requires:	jfreechart = 1.0.14-10.0
Requires:	jpackage-utils
Provides:	jfreechart-swt = 1.0.14-10.0:2014.0

%description	-n jfreechart-swt
jfreechart-swt bootstrap version.

%files		-n jfreechart-swt
/usr/share/java/jfreechart/jfreechart-swt.jar
/usr/share/java/jfreechart/swtgraphics2d.jar

#------------------------------------------------------------------------
%package	-n jfreechart-javadoc
Version:	1.0.14
Release:	10.0
Summary:	jfreechart-javadoc bootstrap version
Requires:	javapackages-bootstrap
Requires:	jfreechart = 1.0.14-10.0
Requires:	jpackage-utils
Provides:	jfreechart-javadoc = 1.0.14-10.0:2014.0

%description	-n jfreechart-javadoc
jfreechart-javadoc bootstrap version.

%files		-n jfreechart-javadoc
/usr/share/javadoc/jfreechart
/usr/share/javadoc/jfreechart/images
/usr/share/javadoc/jfreechart/images/AreaRendererSample.png
/usr/share/javadoc/jfreechart/images/BarRenderer3DSample.png
/usr/share/javadoc/jfreechart/images/BarRendererSample.png
/usr/share/javadoc/jfreechart/images/BoxAndWhiskerRendererSample.png
/usr/share/javadoc/jfreechart/images/CandleStickRendererSample.png
/usr/share/javadoc/jfreechart/images/CategoryStepRendererSample.png
/usr/share/javadoc/jfreechart/images/ClusteredXYBarRendererSample.png
/usr/share/javadoc/jfreechart/images/DeviationRendererSample.png
/usr/share/javadoc/jfreechart/images/DialPlotSample.png
/usr/share/javadoc/jfreechart/images/GanttRendererSample.png
/usr/share/javadoc/jfreechart/images/GroupedStackedBarRendererSample.png
/usr/share/javadoc/jfreechart/images/HighLowRendererSample.png
/usr/share/javadoc/jfreechart/images/IntervalBarRendererSample.png
/usr/share/javadoc/jfreechart/images/LayeredBarRendererSample.png
/usr/share/javadoc/jfreechart/images/LevelRendererSample.png
/usr/share/javadoc/jfreechart/images/LineAndShapeRendererSample.png
/usr/share/javadoc/jfreechart/images/LineRenderer3DSample.png
/usr/share/javadoc/jfreechart/images/MinMaxCategoryRendererSample.png
/usr/share/javadoc/jfreechart/images/PiePlotSample.png
/usr/share/javadoc/jfreechart/images/ScatterRendererSample.png
/usr/share/javadoc/jfreechart/images/StackedAreaRendererSample.png
/usr/share/javadoc/jfreechart/images/StackedBarRenderer3DSample.png
/usr/share/javadoc/jfreechart/images/StackedBarRendererSample.png
/usr/share/javadoc/jfreechart/images/StackedXYAreaRenderer2Sample.png
/usr/share/javadoc/jfreechart/images/StackedXYAreaRendererSample.png
/usr/share/javadoc/jfreechart/images/StackedXYBarRendererSample.png
/usr/share/javadoc/jfreechart/images/StatisticalBarRendererSample.png
/usr/share/javadoc/jfreechart/images/StatisticalLineRendererSample.png
/usr/share/javadoc/jfreechart/images/VectorRendererSample.png
/usr/share/javadoc/jfreechart/images/WaterfallBarRendererSample.png
/usr/share/javadoc/jfreechart/images/WindItemRendererSample.png
/usr/share/javadoc/jfreechart/images/XYAreaRenderer2Sample.png
/usr/share/javadoc/jfreechart/images/XYAreaRendererSample.png
/usr/share/javadoc/jfreechart/images/XYBarRendererSample.png
/usr/share/javadoc/jfreechart/images/XYBlockRendererSample.png
/usr/share/javadoc/jfreechart/images/XYBoxAndWhiskerRendererSample.png
/usr/share/javadoc/jfreechart/images/XYBubbleRendererSample.png
/usr/share/javadoc/jfreechart/images/XYDifferenceRendererSample.png
/usr/share/javadoc/jfreechart/images/XYDotRendererSample.png
/usr/share/javadoc/jfreechart/images/XYErrorRendererSample.png
/usr/share/javadoc/jfreechart/images/XYLineAndShapeRendererSample.png
/usr/share/javadoc/jfreechart/images/XYShapeRendererSample.png
/usr/share/javadoc/jfreechart/images/XYSplineRendererSample.png
/usr/share/javadoc/jfreechart/images/XYStepAreaRendererSample.png
/usr/share/javadoc/jfreechart/images/XYStepRendererSample.png
/usr/share/javadoc/jfreechart/images/YIntervalRendererSample.png

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
rpm2cpio %{SOURCE1} | cpio -id
rpm2cpio %{SOURCE2} | cpio -id
