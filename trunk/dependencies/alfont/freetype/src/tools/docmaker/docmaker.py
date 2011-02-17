#!/usr/bin/env python
#
#  DocMaker 0.2 (c) 2002 David Turner <david@freetype.org>
#
# This program is a re-write of the original DocMaker took used
# to generate the API Reference of the FreeType font engine
# by converting in-source comments into structured HTML
#
# This new version is capable of outputting XML data, as well
# as accepts more liberal formatting options
#
# It also uses regular expression matching and substitution
# to speed things significantly
#

from sources   import *
from content   import *
from utils     import *
from formatter import *
from tohtml    import *

import utils

import sys, os, time, string, glob, getopt


def file_exists( pathname ):
    """checks that a given file exists"""
    result = 1
    try:
        file = open( pathname, "r" )
        file.close()
    except:
        result = None
        sys.stderr.write( pathname + " couldn't be accessed\n" )

    return result


def make_file_list( args = None ):
    """builds a list of input files from command-line arguments"""

    file_list = []
    # sys.stderr.write( repr( sys.argv[1 :] ) + '\n' )

    if not args:
        args = sys.argv[1 :]

    for pathname in args:
        if string.find( pathname, '*' ) >= 0:
            newpath = glob.glob( pathname )
            newpath.sort()  # sort files -- this is important because
                            # of the order of files
        else:
            newpath = [pathname]
            
        file_list.extend( newpath )

    if len( file_list ) == 0:
        file_list = None
    else:
        # now filter the file list to remove non-existing ones
        file_list = filter( file_exists, file_list )
    
    return file_list



def usage():
    print "\nDocMaker 0.2 Usage information\n"
    print "  docmaker [options] file1 [ file2 ... ]\n"
    print "using the following options:\n"
    print "  -h : print this page"
    print "  -t : set project title, as in '-t \"My Project\"'"
    print "  -o : set output directory, as in '-o mydir'"
    print "  -p : set documentation prefix, as in '-p ft2'"
    print ""
    print "  --title  : same as -t, as in '--title=\"My Project\"'"
    print "  --output : same as -o, as in '--output=mydir'"
    print "  --prefix : same as -p, as in '--prefix=ft2'"
    

def main( argv ):
    """main program loop"""

    global output_dir

    try:
        opts, args = getopt.getopt( sys.argv[1:],
                                    "ht:o:p:",
                                    [ "help", "title=", "output=", "prefix=" ] )

    except getopt.GetoptError:
        usage()
        sys.exit( 2 )

    if args == []:
        usage()
        sys.exit( 1 )

    # process options
    #
    project_title  = "Project"
    project_prefix = None
    output_dir     = None

    for opt in opts:
        if opt[0] in ( "-h", "--help" ):
            usage()
            sys.exit( 0 )

        if opt[0] in ( "-t", "--title" ):
            project_title = opt[1]

        if opt[0] in ( "-o", "--output" ):
            utils.output_dir = opt[1]

        if opt[0] in ( "-p", "--prefix" ):
            project_prefix = opt[1]

    check_output( )

    # create context and processor
    source_processor  = SourceProcessor()
    content_processor = ContentProcessor()

    # retrieve the list of files to process
    file_list = make_file_list( args )
    for filename in file_list:
        source_processor.parse_file( filename )
        content_processor.parse_sources( source_processor )
        
    # process sections
    content_processor.finish()

    formatter = HtmlFormatter( content_processor, project_title, project_prefix )

    formatter.toc_dump()
    formatter.index_dump()
    formatter.section_dump_all()


# if called from the command line
#
if __name__ == '__main__':
    main( sys.argv )


# eof
