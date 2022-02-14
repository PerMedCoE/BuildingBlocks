/* A Bison parser, made by GNU Bison 3.5.1.  */

/* Bison implementation for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2020 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with CTBNDL or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Undocumented macros, especially those whose name start with YY_,
   are private implementation details.  Do not rely on them.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "3.5.1"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* First part of user prologue.  */
#line 2 "BooleanGrammar.y"

/*
#############################################################################
#                                                                           #
# BSD 3-Clause License (see https://opensource.org/licenses/BSD-3-Clause)   #
#                                                                           #
# Copyright (c) 2011-2020 Institut Curie, 26 rue d'Ulm, Paris, France       #
# All rights reserved.                                                      #
#                                                                           #
# Redistribution and use in source and binary forms, with or without        #
# modification, are permitted provided that the following conditions are    #
# met:                                                                      #
#                                                                           #
# 1. Redistributions of source code must retain the above copyright notice, #
# this list of conditions and the following disclaimer.                     #
#                                                                           #
# 2. Redistributions in binary form must reproduce the above copyright      #
# notice, this list of conditions and the following disclaimer in the       #
# documentation and/or other materials provided with the distribution.      #
#                                                                           #
# 3. Neither the name of the copyright holder nor the names of its          #
# contributors may be used to endorse or promote products derived from this #
# software without specific prior written permission.                       #
#                                                                           #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS       #
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED #
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A           #
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER #
# OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,  #
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,       #
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR        #
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF    #
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING      #
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS        #
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.              #
#                                                                           #
#############################################################################

   Module:
     BooleanGrammar.y

   Authors:
     Eric Viara <viara@sysra.com>
     Gautier Stoll <gautier.stoll@curie.fr>
     Vincent Noël <vincent.noel@curie.fr> 
   Date:
     January-March 2011
*/

#define _POSIX_SOURCE 1
#include "BooleanGrammar.h"

extern int CTBNDLlex();
static void CTBNDLerror(const char *s);
static Network* current_network;

#line 127 "BooleanGrammar.tab.c"

# ifndef YY_CAST
#  ifdef __cplusplus
#   define YY_CAST(Type, Val) static_cast<Type> (Val)
#   define YY_REINTERPRET_CAST(Type, Val) reinterpret_cast<Type> (Val)
#  else
#   define YY_CAST(Type, Val) ((Type) (Val))
#   define YY_REINTERPRET_CAST(Type, Val) ((Type) (Val))
#  endif
# endif
# ifndef YY_NULLPTR
#  if defined __cplusplus
#   if 201103L <= __cplusplus
#    define YY_NULLPTR nullptr
#   else
#    define YY_NULLPTR 0
#   endif
#  else
#   define YY_NULLPTR ((void*)0)
#  endif
# endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif


/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int CTBNDLdebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum CTBNDLtokentype
  {
    IDENTIFIER = 258,
    VARIABLE = 259,
    STRING = 260,
    DOUBLE = 261,
    INTEGER = 262,
    LOGAND = 263,
    LOGOR = 264,
    LOGXOR = 265,
    LOGNOT = 266,
    EQUAL = 267,
    NOT_EQUAL = 268,
    NODE = 269,
    GTEQ = 270,
    LTEQ = 271
  };
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 59 "BooleanGrammar.y"

  std::vector<NodeDecl*>* node_decl_list;
  NodeDecl* node_decl;
  std::vector<NodeDeclItem*>* node_decl_item_list;
  NodeDeclItem* node_decl_item;
  Expression* expr;
  ArgumentList* arg_list;
  char* str;
  double d;
  long long l;

#line 205 "BooleanGrammar.tab.c"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE CTBNDLlval;

int CTBNDLparse (void);





#ifdef short
# undef short
#endif

/* On compilers that do not define __PTRDIFF_MAX__ etc., make sure
   <limits.h> and (if available) <stdint.h> are included
   so that the code can choose integer types of a good width.  */

#ifndef __PTRDIFF_MAX__
# include <limits.h> /* INFRINGES ON USER NAME SPACE */
# if defined __STDC_VERSION__ && 199901 <= __STDC_VERSION__
#  include <stdint.h> /* INFRINGES ON USER NAME SPACE */
#  define YY_STDINT_H
# endif
#endif

/* Narrow types that promote to a signed type and that can represent a
   signed or unsigned integer of at least N bits.  In tables they can
   save space and decrease cache pressure.  Promoting to a signed type
   helps avoid bugs in integer arithmetic.  */

#ifdef __INT_LEAST8_MAX__
typedef __INT_LEAST8_TYPE__ CTBNDLtype_int8;
#elif defined YY_STDINT_H
typedef int_least8_t CTBNDLtype_int8;
#else
typedef signed char CTBNDLtype_int8;
#endif

#ifdef __INT_LEAST16_MAX__
typedef __INT_LEAST16_TYPE__ CTBNDLtype_int16;
#elif defined YY_STDINT_H
typedef int_least16_t CTBNDLtype_int16;
#else
typedef short CTBNDLtype_int16;
#endif

#if defined __UINT_LEAST8_MAX__ && __UINT_LEAST8_MAX__ <= __INT_MAX__
typedef __UINT_LEAST8_TYPE__ CTBNDLtype_uint8;
#elif (!defined __UINT_LEAST8_MAX__ && defined YY_STDINT_H \
       && UINT_LEAST8_MAX <= INT_MAX)
typedef uint_least8_t CTBNDLtype_uint8;
#elif !defined __UINT_LEAST8_MAX__ && UCHAR_MAX <= INT_MAX
typedef unsigned char CTBNDLtype_uint8;
#else
typedef short CTBNDLtype_uint8;
#endif

#if defined __UINT_LEAST16_MAX__ && __UINT_LEAST16_MAX__ <= __INT_MAX__
typedef __UINT_LEAST16_TYPE__ CTBNDLtype_uint16;
#elif (!defined __UINT_LEAST16_MAX__ && defined YY_STDINT_H \
       && UINT_LEAST16_MAX <= INT_MAX)
typedef uint_least16_t CTBNDLtype_uint16;
#elif !defined __UINT_LEAST16_MAX__ && USHRT_MAX <= INT_MAX
typedef unsigned short CTBNDLtype_uint16;
#else
typedef int CTBNDLtype_uint16;
#endif

#ifndef YYPTRDIFF_T
# if defined __PTRDIFF_TYPE__ && defined __PTRDIFF_MAX__
#  define YYPTRDIFF_T __PTRDIFF_TYPE__
#  define YYPTRDIFF_MAXIMUM __PTRDIFF_MAX__
# elif defined PTRDIFF_MAX
#  ifndef ptrdiff_t
#   include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  endif
#  define YYPTRDIFF_T ptrdiff_t
#  define YYPTRDIFF_MAXIMUM PTRDIFF_MAX
# else
#  define YYPTRDIFF_T long
#  define YYPTRDIFF_MAXIMUM LONG_MAX
# endif
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif defined __STDC_VERSION__ && 199901 <= __STDC_VERSION__
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned
# endif
#endif

#define YYSIZE_MAXIMUM                                  \
  YY_CAST (YYPTRDIFF_T,                                 \
           (YYPTRDIFF_MAXIMUM < YY_CAST (YYSIZE_T, -1)  \
            ? YYPTRDIFF_MAXIMUM                         \
            : YY_CAST (YYSIZE_T, -1)))

#define YYSIZEOF(X) YY_CAST (YYPTRDIFF_T, sizeof (X))

/* Stored state numbers (used for stacks). */
typedef CTBNDLtype_int8 CTBNDL_state_t;

/* State numbers in computations.  */
typedef int CTBNDL_state_fast_t;

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif

#ifndef YY_ATTRIBUTE_PURE
# if defined __GNUC__ && 2 < __GNUC__ + (96 <= __GNUC_MINOR__)
#  define YY_ATTRIBUTE_PURE __attribute__ ((__pure__))
# else
#  define YY_ATTRIBUTE_PURE
# endif
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# if defined __GNUC__ && 2 < __GNUC__ + (7 <= __GNUC_MINOR__)
#  define YY_ATTRIBUTE_UNUSED __attribute__ ((__unused__))
# else
#  define YY_ATTRIBUTE_UNUSED
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(E) ((void) (E))
#else
# define YYUSE(E) /* empty */
#endif

#if defined __GNUC__ && ! defined __ICC && 407 <= __GNUC__ * 100 + __GNUC_MINOR__
/* Suppress an incorrect diagnostic about CTBNDLlval being uninitialized.  */
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN                            \
    _Pragma ("GCC diagnostic push")                                     \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")              \
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# define YY_IGNORE_MAYBE_UNINITIALIZED_END      \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif

#if defined __cplusplus && defined __GNUC__ && ! defined __ICC && 6 <= __GNUC__
# define YY_IGNORE_USELESS_CAST_BEGIN                          \
    _Pragma ("GCC diagnostic push")                            \
    _Pragma ("GCC diagnostic ignored \"-Wuseless-cast\"")
# define YY_IGNORE_USELESS_CAST_END            \
    _Pragma ("GCC diagnostic pop")
#endif
#ifndef YY_IGNORE_USELESS_CAST_BEGIN
# define YY_IGNORE_USELESS_CAST_BEGIN
# define YY_IGNORE_USELESS_CAST_END
#endif


#define YY_ASSERT(E) ((void) (0 && (E)))

#if ! defined CTBNDLoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined CTBNDLoverflow || YYERROR_VERBOSE */


#if (! defined CTBNDLoverflow \
     && (! defined __cplusplus \
         || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union CTBNDLalloc
{
  CTBNDL_state_t CTBNDLss_alloc;
  YYSTYPE CTBNDLvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (YYSIZEOF (union CTBNDLalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (YYSIZEOF (CTBNDL_state_t) + YYSIZEOF (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYPTRDIFF_T CTBNDLnewbytes;                                         \
        YYCOPY (&CTBNDLptr->Stack_alloc, Stack, CTBNDLsize);                    \
        Stack = &CTBNDLptr->Stack_alloc;                                    \
        CTBNDLnewbytes = CTBNDLstacksize * YYSIZEOF (*Stack) + YYSTACK_GAP_MAXIMUM; \
        CTBNDLptr += CTBNDLnewbytes / YYSIZEOF (*CTBNDLptr);                        \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, YY_CAST (YYSIZE_T, (Count)) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYPTRDIFF_T CTBNDLi;                      \
          for (CTBNDLi = 0; CTBNDLi < (Count); CTBNDLi++)   \
            (Dst)[CTBNDLi] = (Src)[CTBNDLi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  9
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   99

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  35
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  20
/* YYNRULES -- Number of rules.  */
#define YYNRULES  54
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  93

#define YYUNDEFTOK  2
#define YYMAXUTOK   271


/* YYTRANSLATE(TOKEN-NUM) -- Symbol number corresponding to TOKEN-NUM
   as returned by CTBNDLlex, with out-of-bounds checking.  */
#define YYTRANSLATE(YYX)                                                \
  (0 <= (YYX) && (YYX) <= YYMAXUTOK ? CTBNDLtranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by CTBNDLlex.  */
static const CTBNDLtype_int8 CTBNDLtranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,    28,     2,     2,     2,     2,     2,     2,
      24,    25,    29,    26,    20,    27,     2,    30,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    19,    22,
      31,    21,    32,    34,    23,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,    33,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,    17,     2,    18,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16
};

#if YYDEBUG
  /* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const CTBNDLtype_int16 CTBNDLrline[] =
{
       0,    98,    98,   101,   106,   116,   122,   138,   140,   144,
     149,   156,   161,   168,   174,   179,   184,   188,   192,   198,
     202,   207,   214,   219,   226,   230,   234,   238,   242,   248,
     252,   256,   262,   266,   270,   276,   280,   284,   288,   292,
     298,   302,   306,   312,   316,   322,   326,   332,   336,   340,
     346,   350,   356,   362,   363
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || 0
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const CTBNDLtname[] =
{
  "$end", "error", "$undefined", "IDENTIFIER", "VARIABLE", "STRING",
  "DOUBLE", "INTEGER", "LOGAND", "LOGOR", "LOGXOR", "LOGNOT", "EQUAL",
  "NOT_EQUAL", "NODE", "GTEQ", "LTEQ", "'{'", "'}'", "':'", "','", "'='",
  "';'", "'@'", "'('", "')'", "'+'", "'-'", "'!'", "'*'", "'/'", "'<'",
  "'>'", "'^'", "'?'", "$accept", "translation_unit", "node_decl",
  "colon_comma", "node_decl_item_list", "node_decl_item",
  "primary_expression", "postfix_expression", "argument_expression_list",
  "unary_expression", "multiplicative_expression", "additive_expression",
  "relational_expression", "equality_expression", "logical_and_expression",
  "logical_or_expression", "logical_xor_expression",
  "conditional_expression", "expression", "term_opt", YY_NULLPTR
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[NUM] -- (External) token number corresponding to the
   (internal) symbol number NUM (which must be that of a token).  */
static const CTBNDLtype_int16 CTBNDLtoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   123,   125,    58,
      44,    61,    59,    64,    40,    41,    43,    45,    33,    42,
      47,    60,    62,    94,    63
};
# endif

#define YYPACT_NINF (-34)

#define CTBNDLpact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-1)

#define CTBNDLtable_value_is_error(Yyn) \
  0

  /* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
     STATE-NUM.  */
static const CTBNDLtype_int8 CTBNDLpact[] =
{
       1,    36,     0,    58,   -34,   -34,   -34,    43,    -1,   -34,
     -34,    21,   -34,   -34,   -34,    43,    45,    43,    43,    43,
      43,   -34,   -34,   -34,    33,    51,    -7,    67,    49,    56,
      26,   -34,    46,    23,     7,   -34,   -34,    61,   -34,   -34,
     -34,    43,    43,    43,    43,    43,    43,    43,    43,    43,
      43,    43,    43,    43,    43,    43,   -34,   -34,    62,   -34,
      34,   -34,   -34,    -8,   -34,   -34,   -34,   -34,    33,    33,
      51,    51,    51,    51,    -7,    -7,    67,    49,    56,    56,
      68,    16,   -34,   -34,    43,   -34,    43,    66,    70,   -34,
     -34,   -34,   -34
};

  /* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
     Performed when YYTABLE does not specify something else to do.  Zero
     means the default is an error.  */
static const CTBNDLtype_int8 CTBNDLdefact[] =
{
       0,     0,     0,     0,     2,     7,     8,     0,     0,     1,
       3,    13,    15,    17,    16,     0,     0,     0,     0,     0,
       0,    19,    24,    29,    32,    35,    40,    43,    45,    47,
      50,    52,    53,     0,     0,    28,    14,     0,    25,    26,
      27,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    54,     6,     0,     5,
       0,     9,    21,     0,    22,    18,    30,    31,    33,    34,
      39,    38,    36,    37,    41,    42,    44,    46,    48,    49,
       0,     0,     4,    10,     0,    20,     0,     0,     0,    23,
      51,    12,    11
};

  /* YYPGOTO[NTERM-NUM].  */
static const CTBNDLtype_int8 CTBNDLpgoto[] =
{
     -34,   -34,    86,   -34,   -34,    39,   -34,   -34,   -34,   -13,
      38,    28,    35,    42,    44,    37,   -34,   -33,   -17,   -34
};

  /* YYDEFGOTO[NTERM-NUM].  */
static const CTBNDLtype_int8 CTBNDLdefgoto[] =
{
      -1,     3,     4,     7,    60,    61,    21,    22,    63,    23,
      24,    25,    26,    27,    28,    29,    30,    31,    32,    57
};

  /* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
     positive, shift that token.  If negative, reduce the rule whose
     number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const CTBNDLtype_int8 CTBNDLtable[] =
{
      37,    64,    35,     8,     1,    38,    39,    40,    45,    46,
      11,    12,    84,    13,    14,     2,    33,    85,    15,    11,
      12,    87,    13,    14,    47,    48,    58,    15,    66,    67,
      16,    17,    62,    18,    19,    20,    53,    58,    80,    16,
      17,    59,    18,    19,    20,    34,    11,    12,    36,    13,
      14,    89,    82,    90,    15,     5,     6,    51,     9,    54,
      55,     1,    41,    42,    88,    52,    16,    17,    56,    18,
      19,    20,     2,    70,    71,    72,    73,    43,    44,    49,
      50,    68,    69,    81,    74,    75,    65,    86,    91,    10,
      78,    79,    92,    76,     0,     0,    77,     0,     0,    83
};

static const CTBNDLtype_int8 CTBNDLcheck[] =
{
      17,    34,    15,     3,     3,    18,    19,    20,    15,    16,
       3,     4,    20,     6,     7,    14,    17,    25,    11,     3,
       4,     5,     6,     7,    31,    32,     3,    11,    41,    42,
      23,    24,    25,    26,    27,    28,    10,     3,    55,    23,
      24,    18,    26,    27,    28,    24,     3,     4,     3,     6,
       7,    84,    18,    86,    11,    19,    20,     8,     0,    33,
      34,     3,    29,    30,    81,     9,    23,    24,    22,    26,
      27,    28,    14,    45,    46,    47,    48,    26,    27,    12,
      13,    43,    44,    21,    49,    50,    25,    19,    22,     3,
      53,    54,    22,    51,    -1,    -1,    52,    -1,    -1,    60
};

  /* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
     symbol of state STATE-NUM.  */
static const CTBNDLtype_int8 CTBNDLstos[] =
{
       0,     3,    14,    36,    37,    19,    20,    38,     3,     0,
      37,     3,     4,     6,     7,    11,    23,    24,    26,    27,
      28,    41,    42,    44,    45,    46,    47,    48,    49,    50,
      51,    52,    53,    17,    24,    44,     3,    53,    44,    44,
      44,    29,    30,    26,    27,    15,    16,    31,    32,    12,
      13,     8,     9,    10,    33,    34,    22,    54,     3,    18,
      39,    40,    25,    43,    52,    25,    44,    44,    45,    45,
      46,    46,    46,    46,    47,    47,    48,    49,    50,    50,
      53,    21,    18,    40,    20,    25,    19,     5,    53,    52,
      52,    22,    22
};

  /* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const CTBNDLtype_int8 CTBNDLr1[] =
{
       0,    35,    36,    36,    37,    37,    37,    38,    38,    39,
      39,    40,    40,    41,    41,    41,    41,    41,    41,    42,
      42,    42,    43,    43,    44,    44,    44,    44,    44,    45,
      45,    45,    46,    46,    46,    47,    47,    47,    47,    47,
      48,    48,    48,    49,    49,    50,    50,    51,    51,    51,
      52,    52,    53,    54,    54
};

  /* YYR2[YYN] -- Number of symbols on the right hand side of rule YYN.  */
static const CTBNDLtype_int8 CTBNDLr2[] =
{
       0,     2,     1,     2,     5,     4,     4,     1,     1,     1,
       2,     4,     4,     1,     2,     1,     1,     1,     3,     1,
       4,     3,     1,     3,     1,     2,     2,     2,     2,     1,
       3,     3,     1,     3,     3,     1,     3,     3,     3,     3,
       1,     3,     3,     1,     3,     1,     3,     1,     3,     3,
       1,     5,     1,     0,     1
};


#define CTBNDLerrok         (CTBNDLerrstatus = 0)
#define CTBNDLclearin       (CTBNDLchar = YYEMPTY)
#define YYEMPTY         (-2)
#define YYEOF           0

#define YYACCEPT        goto CTBNDLacceptlab
#define YYABORT         goto CTBNDLabortlab
#define YYERROR         goto CTBNDLerrorlab


#define YYRECOVERING()  (!!CTBNDLerrstatus)

#define YYBACKUP(Token, Value)                                    \
  do                                                              \
    if (CTBNDLchar == YYEMPTY)                                        \
      {                                                           \
        CTBNDLchar = (Token);                                         \
        CTBNDLlval = (Value);                                         \
        YYPOPSTACK (CTBNDLlen);                                       \
        CTBNDLstate = *CTBNDLssp;                                         \
        goto CTBNDLbackup;                                            \
      }                                                           \
    else                                                          \
      {                                                           \
        CTBNDLerror (YY_("syntax error: cannot back up")); \
        YYERROR;                                                  \
      }                                                           \
  while (0)

/* Error token number */
#define YYTERROR        1
#define YYERRCODE       256



/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (CTBNDLdebug)                                  \
    YYFPRINTF Args;                             \
} while (0)

/* This macro is provided for backward compatibility. */
#ifndef YY_LOCATION_PRINT
# define YY_LOCATION_PRINT(File, Loc) ((void) 0)
#endif


# define YY_SYMBOL_PRINT(Title, Type, Value, Location)                    \
do {                                                                      \
  if (CTBNDLdebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      CTBNDL_symbol_print (stderr,                                            \
                  Type, Value); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*-----------------------------------.
| Print this symbol's value on YYO.  |
`-----------------------------------*/

static void
CTBNDL_symbol_value_print (FILE *CTBNDLo, int CTBNDLtype, YYSTYPE const * const CTBNDLvaluep)
{
  FILE *CTBNDLoutput = CTBNDLo;
  YYUSE (CTBNDLoutput);
  if (!CTBNDLvaluep)
    return;
# ifdef YYPRINT
  if (CTBNDLtype < YYNTOKENS)
    YYPRINT (CTBNDLo, CTBNDLtoknum[CTBNDLtype], *CTBNDLvaluep);
# endif
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (CTBNDLtype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}


/*---------------------------.
| Print this symbol on YYO.  |
`---------------------------*/

static void
CTBNDL_symbol_print (FILE *CTBNDLo, int CTBNDLtype, YYSTYPE const * const CTBNDLvaluep)
{
  YYFPRINTF (CTBNDLo, "%s %s (",
             CTBNDLtype < YYNTOKENS ? "token" : "nterm", CTBNDLtname[CTBNDLtype]);

  CTBNDL_symbol_value_print (CTBNDLo, CTBNDLtype, CTBNDLvaluep);
  YYFPRINTF (CTBNDLo, ")");
}

/*------------------------------------------------------------------.
| CTBNDL_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
CTBNDL_stack_print (CTBNDL_state_t *CTBNDLbottom, CTBNDL_state_t *CTBNDLtop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; CTBNDLbottom <= CTBNDLtop; CTBNDLbottom++)
    {
      int CTBNDLbot = *CTBNDLbottom;
      YYFPRINTF (stderr, " %d", CTBNDLbot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (CTBNDLdebug)                                                  \
    CTBNDL_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
CTBNDL_reduce_print (CTBNDL_state_t *CTBNDLssp, YYSTYPE *CTBNDLvsp, int CTBNDLrule)
{
  int CTBNDLlno = CTBNDLrline[CTBNDLrule];
  int CTBNDLnrhs = CTBNDLr2[CTBNDLrule];
  int CTBNDLi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %d):\n",
             CTBNDLrule - 1, CTBNDLlno);
  /* The symbols being reduced.  */
  for (CTBNDLi = 0; CTBNDLi < CTBNDLnrhs; CTBNDLi++)
    {
      YYFPRINTF (stderr, "   $%d = ", CTBNDLi + 1);
      CTBNDL_symbol_print (stderr,
                       CTBNDLstos[+CTBNDLssp[CTBNDLi + 1 - CTBNDLnrhs]],
                       &CTBNDLvsp[(CTBNDLi + 1) - (CTBNDLnrhs)]
                                              );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (CTBNDLdebug)                          \
    CTBNDL_reduce_print (CTBNDLssp, CTBNDLvsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int CTBNDLdebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


#if YYERROR_VERBOSE

# ifndef CTBNDLstrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define CTBNDLstrlen(S) (YY_CAST (YYPTRDIFF_T, strlen (S)))
#  else
/* Return the length of YYSTR.  */
static YYPTRDIFF_T
CTBNDLstrlen (const char *CTBNDLstr)
{
  YYPTRDIFF_T CTBNDLlen;
  for (CTBNDLlen = 0; CTBNDLstr[CTBNDLlen]; CTBNDLlen++)
    continue;
  return CTBNDLlen;
}
#  endif
# endif

# ifndef CTBNDLstpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define CTBNDLstpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
static char *
CTBNDLstpcpy (char *CTBNDLdest, const char *CTBNDLsrc)
{
  char *CTBNDLd = CTBNDLdest;
  const char *CTBNDLs = CTBNDLsrc;

  while ((*CTBNDLd++ = *CTBNDLs++) != '\0')
    continue;

  return CTBNDLd - 1;
}
#  endif
# endif

# ifndef CTBNDLtnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for CTBNDLerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from CTBNDLtname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYPTRDIFF_T
CTBNDLtnamerr (char *CTBNDLres, const char *CTBNDLstr)
{
  if (*CTBNDLstr == '"')
    {
      YYPTRDIFF_T CTBNDLn = 0;
      char const *CTBNDLp = CTBNDLstr;

      for (;;)
        switch (*++CTBNDLp)
          {
          case '\'':
          case ',':
            goto do_not_strip_quotes;

          case '\\':
            if (*++CTBNDLp != '\\')
              goto do_not_strip_quotes;
            else
              goto append;

          append:
          default:
            if (CTBNDLres)
              CTBNDLres[CTBNDLn] = *CTBNDLp;
            CTBNDLn++;
            break;

          case '"':
            if (CTBNDLres)
              CTBNDLres[CTBNDLn] = '\0';
            return CTBNDLn;
          }
    do_not_strip_quotes: ;
    }

  if (CTBNDLres)
    return CTBNDLstpcpy (CTBNDLres, CTBNDLstr) - CTBNDLres;
  else
    return CTBNDLstrlen (CTBNDLstr);
}
# endif

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return 1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return 2 if the
   required number of bytes is too large to store.  */
static int
CTBNDLsyntax_error (YYPTRDIFF_T *CTBNDLmsg_alloc, char **CTBNDLmsg,
                CTBNDL_state_t *CTBNDLssp, int CTBNDLtoken)
{
  enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
  /* Internationalized format string. */
  const char *CTBNDLformat = YY_NULLPTR;
  /* Arguments of CTBNDLformat: reported tokens (one for the "unexpected",
     one per "expected"). */
  char const *CTBNDLarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
  /* Actual size of YYARG. */
  int CTBNDLcount = 0;
  /* Cumulated lengths of YYARG.  */
  YYPTRDIFF_T CTBNDLsize = 0;

  /* There are many possibilities here to consider:
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in CTBNDLchar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated CTBNDLchar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (CTBNDLtoken != YYEMPTY)
    {
      int CTBNDLn = CTBNDLpact[+*CTBNDLssp];
      YYPTRDIFF_T CTBNDLsize0 = CTBNDLtnamerr (YY_NULLPTR, CTBNDLtname[CTBNDLtoken]);
      CTBNDLsize = CTBNDLsize0;
      CTBNDLarg[CTBNDLcount++] = CTBNDLtname[CTBNDLtoken];
      if (!CTBNDLpact_value_is_default (CTBNDLn))
        {
          /* Start YYX at -YYN if negative to avoid negative indexes in
             YYCHECK.  In other words, skip the first -YYN actions for
             this state because they are default actions.  */
          int CTBNDLxbegin = CTBNDLn < 0 ? -CTBNDLn : 0;
          /* Stay within bounds of both CTBNDLcheck and CTBNDLtname.  */
          int CTBNDLchecklim = YYLAST - CTBNDLn + 1;
          int CTBNDLxend = CTBNDLchecklim < YYNTOKENS ? CTBNDLchecklim : YYNTOKENS;
          int CTBNDLx;

          for (CTBNDLx = CTBNDLxbegin; CTBNDLx < CTBNDLxend; ++CTBNDLx)
            if (CTBNDLcheck[CTBNDLx + CTBNDLn] == CTBNDLx && CTBNDLx != YYTERROR
                && !CTBNDLtable_value_is_error (CTBNDLtable[CTBNDLx + CTBNDLn]))
              {
                if (CTBNDLcount == YYERROR_VERBOSE_ARGS_MAXIMUM)
                  {
                    CTBNDLcount = 1;
                    CTBNDLsize = CTBNDLsize0;
                    break;
                  }
                CTBNDLarg[CTBNDLcount++] = CTBNDLtname[CTBNDLx];
                {
                  YYPTRDIFF_T CTBNDLsize1
                    = CTBNDLsize + CTBNDLtnamerr (YY_NULLPTR, CTBNDLtname[CTBNDLx]);
                  if (CTBNDLsize <= CTBNDLsize1 && CTBNDLsize1 <= YYSTACK_ALLOC_MAXIMUM)
                    CTBNDLsize = CTBNDLsize1;
                  else
                    return 2;
                }
              }
        }
    }

  switch (CTBNDLcount)
    {
# define YYCASE_(N, S)                      \
      case N:                               \
        CTBNDLformat = S;                       \
      break
    default: /* Avoid compiler warnings. */
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
# undef YYCASE_
    }

  {
    /* Don't count the "%s"s in the final size, but reserve room for
       the terminator.  */
    YYPTRDIFF_T CTBNDLsize1 = CTBNDLsize + (CTBNDLstrlen (CTBNDLformat) - 2 * CTBNDLcount) + 1;
    if (CTBNDLsize <= CTBNDLsize1 && CTBNDLsize1 <= YYSTACK_ALLOC_MAXIMUM)
      CTBNDLsize = CTBNDLsize1;
    else
      return 2;
  }

  if (*CTBNDLmsg_alloc < CTBNDLsize)
    {
      *CTBNDLmsg_alloc = 2 * CTBNDLsize;
      if (! (CTBNDLsize <= *CTBNDLmsg_alloc
             && *CTBNDLmsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *CTBNDLmsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return 1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *CTBNDLp = *CTBNDLmsg;
    int CTBNDLi = 0;
    while ((*CTBNDLp = *CTBNDLformat) != '\0')
      if (*CTBNDLp == '%' && CTBNDLformat[1] == 's' && CTBNDLi < CTBNDLcount)
        {
          CTBNDLp += CTBNDLtnamerr (CTBNDLp, CTBNDLarg[CTBNDLi++]);
          CTBNDLformat += 2;
        }
      else
        {
          ++CTBNDLp;
          ++CTBNDLformat;
        }
  }
  return 0;
}
#endif /* YYERROR_VERBOSE */

/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
CTBNDLdestruct (const char *CTBNDLmsg, int CTBNDLtype, YYSTYPE *CTBNDLvaluep)
{
  YYUSE (CTBNDLvaluep);
  if (!CTBNDLmsg)
    CTBNDLmsg = "Deleting";
  YY_SYMBOL_PRINT (CTBNDLmsg, CTBNDLtype, CTBNDLvaluep, CTBNDLlocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (CTBNDLtype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}




/* The lookahead symbol.  */
int CTBNDLchar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE CTBNDLlval;
/* Number of syntax errors so far.  */
int CTBNDLnerrs;


/*----------.
| CTBNDLparse.  |
`----------*/

int
CTBNDLparse (void)
{
    CTBNDL_state_fast_t CTBNDLstate;
    /* Number of tokens to shift before error messages enabled.  */
    int CTBNDLerrstatus;

    /* The stacks and their tools:
       'CTBNDLss': related to states.
       'CTBNDLvs': related to semantic values.

       Refer to the stacks through separate pointers, to allow CTBNDLoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    CTBNDL_state_t CTBNDLssa[YYINITDEPTH];
    CTBNDL_state_t *CTBNDLss;
    CTBNDL_state_t *CTBNDLssp;

    /* The semantic value stack.  */
    YYSTYPE CTBNDLvsa[YYINITDEPTH];
    YYSTYPE *CTBNDLvs;
    YYSTYPE *CTBNDLvsp;

    YYPTRDIFF_T CTBNDLstacksize;

  int CTBNDLn;
  int CTBNDLresult;
  /* Lookahead token as an internal (translated) token number.  */
  int CTBNDLtoken = 0;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE CTBNDLval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char CTBNDLmsgbuf[128];
  char *CTBNDLmsg = CTBNDLmsgbuf;
  YYPTRDIFF_T CTBNDLmsg_alloc = sizeof CTBNDLmsgbuf;
#endif

#define YYPOPSTACK(N)   (CTBNDLvsp -= (N), CTBNDLssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int CTBNDLlen = 0;

  CTBNDLssp = CTBNDLss = CTBNDLssa;
  CTBNDLvsp = CTBNDLvs = CTBNDLvsa;
  CTBNDLstacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  CTBNDLstate = 0;
  CTBNDLerrstatus = 0;
  CTBNDLnerrs = 0;
  CTBNDLchar = YYEMPTY; /* Cause a token to be read.  */
  goto CTBNDLsetstate;


/*------------------------------------------------------------.
| CTBNDLnewstate -- push a new state, which is found in CTBNDLstate.  |
`------------------------------------------------------------*/
CTBNDLnewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  CTBNDLssp++;


/*--------------------------------------------------------------------.
| CTBNDLsetstate -- set current state (the top of the stack) to CTBNDLstate.  |
`--------------------------------------------------------------------*/
CTBNDLsetstate:
  YYDPRINTF ((stderr, "Entering state %d\n", CTBNDLstate));
  YY_ASSERT (0 <= CTBNDLstate && CTBNDLstate < YYNSTATES);
  YY_IGNORE_USELESS_CAST_BEGIN
  *CTBNDLssp = YY_CAST (CTBNDL_state_t, CTBNDLstate);
  YY_IGNORE_USELESS_CAST_END

  if (CTBNDLss + CTBNDLstacksize - 1 <= CTBNDLssp)
#if !defined CTBNDLoverflow && !defined YYSTACK_RELOCATE
    goto CTBNDLexhaustedlab;
#else
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYPTRDIFF_T CTBNDLsize = CTBNDLssp - CTBNDLss + 1;

# if defined CTBNDLoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        CTBNDL_state_t *CTBNDLss1 = CTBNDLss;
        YYSTYPE *CTBNDLvs1 = CTBNDLvs;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if CTBNDLoverflow is a macro.  */
        CTBNDLoverflow (YY_("memory exhausted"),
                    &CTBNDLss1, CTBNDLsize * YYSIZEOF (*CTBNDLssp),
                    &CTBNDLvs1, CTBNDLsize * YYSIZEOF (*CTBNDLvsp),
                    &CTBNDLstacksize);
        CTBNDLss = CTBNDLss1;
        CTBNDLvs = CTBNDLvs1;
      }
# else /* defined YYSTACK_RELOCATE */
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= CTBNDLstacksize)
        goto CTBNDLexhaustedlab;
      CTBNDLstacksize *= 2;
      if (YYMAXDEPTH < CTBNDLstacksize)
        CTBNDLstacksize = YYMAXDEPTH;

      {
        CTBNDL_state_t *CTBNDLss1 = CTBNDLss;
        union CTBNDLalloc *CTBNDLptr =
          YY_CAST (union CTBNDLalloc *,
                   YYSTACK_ALLOC (YY_CAST (YYSIZE_T, YYSTACK_BYTES (CTBNDLstacksize))));
        if (! CTBNDLptr)
          goto CTBNDLexhaustedlab;
        YYSTACK_RELOCATE (CTBNDLss_alloc, CTBNDLss);
        YYSTACK_RELOCATE (CTBNDLvs_alloc, CTBNDLvs);
# undef YYSTACK_RELOCATE
        if (CTBNDLss1 != CTBNDLssa)
          YYSTACK_FREE (CTBNDLss1);
      }
# endif

      CTBNDLssp = CTBNDLss + CTBNDLsize - 1;
      CTBNDLvsp = CTBNDLvs + CTBNDLsize - 1;

      YY_IGNORE_USELESS_CAST_BEGIN
      YYDPRINTF ((stderr, "Stack size increased to %ld\n",
                  YY_CAST (long, CTBNDLstacksize)));
      YY_IGNORE_USELESS_CAST_END

      if (CTBNDLss + CTBNDLstacksize - 1 <= CTBNDLssp)
        YYABORT;
    }
#endif /* !defined CTBNDLoverflow && !defined YYSTACK_RELOCATE */

  if (CTBNDLstate == YYFINAL)
    YYACCEPT;

  goto CTBNDLbackup;


/*-----------.
| CTBNDLbackup.  |
`-----------*/
CTBNDLbackup:
  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  CTBNDLn = CTBNDLpact[CTBNDLstate];
  if (CTBNDLpact_value_is_default (CTBNDLn))
    goto CTBNDLdefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (CTBNDLchar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      CTBNDLchar = CTBNDLlex ();
    }

  if (CTBNDLchar <= YYEOF)
    {
      CTBNDLchar = CTBNDLtoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      CTBNDLtoken = YYTRANSLATE (CTBNDLchar);
      YY_SYMBOL_PRINT ("Next token is", CTBNDLtoken, &CTBNDLlval, &CTBNDLlloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  CTBNDLn += CTBNDLtoken;
  if (CTBNDLn < 0 || YYLAST < CTBNDLn || CTBNDLcheck[CTBNDLn] != CTBNDLtoken)
    goto CTBNDLdefault;
  CTBNDLn = CTBNDLtable[CTBNDLn];
  if (CTBNDLn <= 0)
    {
      if (CTBNDLtable_value_is_error (CTBNDLn))
        goto CTBNDLerrlab;
      CTBNDLn = -CTBNDLn;
      goto CTBNDLreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (CTBNDLerrstatus)
    CTBNDLerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", CTBNDLtoken, &CTBNDLlval, &CTBNDLlloc);
  CTBNDLstate = CTBNDLn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++CTBNDLvsp = CTBNDLlval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  /* Discard the shifted token.  */
  CTBNDLchar = YYEMPTY;
  goto CTBNDLnewstate;


/*-----------------------------------------------------------.
| CTBNDLdefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
CTBNDLdefault:
  CTBNDLn = CTBNDLdefact[CTBNDLstate];
  if (CTBNDLn == 0)
    goto CTBNDLerrlab;
  goto CTBNDLreduce;


/*-----------------------------.
| CTBNDLreduce -- do a reduction.  |
`-----------------------------*/
CTBNDLreduce:
  /* CTBNDLn is the number of a rule to reduce with.  */
  CTBNDLlen = CTBNDLr2[CTBNDLn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  CTBNDLval = CTBNDLvsp[1-CTBNDLlen];


  YY_REDUCE_PRINT (CTBNDLn);
  switch (CTBNDLn)
    {
  case 2:
#line 99 "BooleanGrammar.y"
{
}
#line 1444 "BooleanGrammar.tab.c"
    break;

  case 3:
#line 102 "BooleanGrammar.y"
{
}
#line 1451 "BooleanGrammar.tab.c"
    break;

  case 4:
#line 107 "BooleanGrammar.y"
{
  NodeDecl* truc = new NodeDecl((CTBNDLvsp[-3].str), (CTBNDLvsp[-1].node_decl_item_list));
  free((CTBNDLvsp[-3].str));
  for (std::vector<NodeDeclItem*>::iterator it = (CTBNDLvsp[-1].node_decl_item_list)->begin(); it != (CTBNDLvsp[-1].node_decl_item_list)->end(); ++it) {
    delete *it;
  }
  delete (CTBNDLvsp[-1].node_decl_item_list);
  delete truc;
}
#line 1465 "BooleanGrammar.tab.c"
    break;

  case 5:
#line 117 "BooleanGrammar.y"
{
  NodeDecl* truc = new NodeDecl((CTBNDLvsp[-2].str), NULL);
  free((CTBNDLvsp[-2].str));
  delete truc;
}
#line 1475 "BooleanGrammar.tab.c"
    break;

  case 6:
#line 123 "BooleanGrammar.y"
{
  NodeDeclItem* decl_item = new NodeDeclItem("logic", (CTBNDLvsp[-1].expr));
  std::vector<NodeDeclItem*>* decl_item_v = new std::vector<NodeDeclItem*>();
  decl_item_v->push_back(decl_item);

  NodeDecl* truc = new NodeDecl((CTBNDLvsp[-3].str), decl_item_v);
  free((CTBNDLvsp[-3].str));
  for (std::vector<NodeDeclItem*>::iterator it = decl_item_v->begin(); it != decl_item_v->end(); ++it) {
    delete *it;
  }
  delete decl_item_v;
  delete truc;
}
#line 1493 "BooleanGrammar.tab.c"
    break;

  case 7:
#line 139 "BooleanGrammar.y"
{}
#line 1499 "BooleanGrammar.tab.c"
    break;

  case 8:
#line 141 "BooleanGrammar.y"
{}
#line 1505 "BooleanGrammar.tab.c"
    break;

  case 9:
#line 145 "BooleanGrammar.y"
{
  (CTBNDLval.node_decl_item_list) = new std::vector<NodeDeclItem*>();
  (CTBNDLval.node_decl_item_list)->push_back((CTBNDLvsp[0].node_decl_item));
}
#line 1514 "BooleanGrammar.tab.c"
    break;

  case 10:
#line 150 "BooleanGrammar.y"
{
  (CTBNDLvsp[-1].node_decl_item_list)->push_back((CTBNDLvsp[0].node_decl_item));
  (CTBNDLval.node_decl_item_list) = (CTBNDLvsp[-1].node_decl_item_list);
}
#line 1523 "BooleanGrammar.tab.c"
    break;

  case 11:
#line 157 "BooleanGrammar.y"
{
  (CTBNDLval.node_decl_item) = new NodeDeclItem((CTBNDLvsp[-3].str), (CTBNDLvsp[-1].expr));
  free((CTBNDLvsp[-3].str));
}
#line 1532 "BooleanGrammar.tab.c"
    break;

  case 12:
#line 162 "BooleanGrammar.y"
{
  (CTBNDLval.node_decl_item) = new NodeDeclItem((CTBNDLvsp[-3].str), (CTBNDLvsp[-1].str));
  free((CTBNDLvsp[-3].str));
}
#line 1541 "BooleanGrammar.tab.c"
    break;

  case 13:
#line 169 "BooleanGrammar.y"
{
  Node* node = current_network->getOrMakeNode((CTBNDLvsp[0].str));
  (CTBNDLval.expr) = new NodeExpression(node);
  free((CTBNDLvsp[0].str));
}
#line 1551 "BooleanGrammar.tab.c"
    break;

  case 14:
#line 175 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new AliasExpression((CTBNDLvsp[0].str));
  free((CTBNDLvsp[0].str));
}
#line 1560 "BooleanGrammar.tab.c"
    break;

  case 15:
#line 180 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new SymbolExpression(current_network->getSymbolTable(), current_network->getSymbolTable()->getOrMakeSymbol((CTBNDLvsp[0].str)));
  free((CTBNDLvsp[0].str));
}
#line 1569 "BooleanGrammar.tab.c"
    break;

  case 16:
#line 185 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new ConstantExpression((CTBNDLvsp[0].l));
}
#line 1577 "BooleanGrammar.tab.c"
    break;

  case 17:
#line 189 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new ConstantExpression((CTBNDLvsp[0].d));
}
#line 1585 "BooleanGrammar.tab.c"
    break;

  case 18:
#line 193 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new ParenthesisExpression((CTBNDLvsp[-1].expr));
}
#line 1593 "BooleanGrammar.tab.c"
    break;

  case 19:
#line 199 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = (CTBNDLvsp[0].expr);
}
#line 1601 "BooleanGrammar.tab.c"
    break;

  case 20:
#line 203 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new FuncCallExpression((CTBNDLvsp[-3].str), (CTBNDLvsp[-1].arg_list));
  free((CTBNDLvsp[-3].str));
}
#line 1610 "BooleanGrammar.tab.c"
    break;

  case 21:
#line 208 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new FuncCallExpression((CTBNDLvsp[-2].str), NULL);
  free((CTBNDLvsp[-2].str));
}
#line 1619 "BooleanGrammar.tab.c"
    break;

  case 22:
#line 215 "BooleanGrammar.y"
{
  (CTBNDLval.arg_list) = new ArgumentList();
  (CTBNDLval.arg_list)->push_back((CTBNDLvsp[0].expr));
}
#line 1628 "BooleanGrammar.tab.c"
    break;

  case 23:
#line 220 "BooleanGrammar.y"
{
  (CTBNDLval.arg_list) = (CTBNDLvsp[-2].arg_list);
  (CTBNDLval.arg_list)->push_back((CTBNDLvsp[0].expr));
}
#line 1637 "BooleanGrammar.tab.c"
    break;

  case 24:
#line 227 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = (CTBNDLvsp[0].expr);
}
#line 1645 "BooleanGrammar.tab.c"
    break;

  case 25:
#line 231 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = (CTBNDLvsp[0].expr);
}
#line 1653 "BooleanGrammar.tab.c"
    break;

  case 26:
#line 235 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new SubExpression(new ConstantExpression(0.0), (CTBNDLvsp[0].expr));
}
#line 1661 "BooleanGrammar.tab.c"
    break;

  case 27:
#line 239 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new NotLogicalExpression((CTBNDLvsp[0].expr));
}
#line 1669 "BooleanGrammar.tab.c"
    break;

  case 28:
#line 243 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new NotLogicalExpression((CTBNDLvsp[0].expr));
}
#line 1677 "BooleanGrammar.tab.c"
    break;

  case 29:
#line 249 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = (CTBNDLvsp[0].expr);
}
#line 1685 "BooleanGrammar.tab.c"
    break;

  case 30:
#line 253 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new MulExpression((CTBNDLvsp[-2].expr), (CTBNDLvsp[0].expr));
}
#line 1693 "BooleanGrammar.tab.c"
    break;

  case 31:
#line 257 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new DivExpression((CTBNDLvsp[-2].expr), (CTBNDLvsp[0].expr));
}
#line 1701 "BooleanGrammar.tab.c"
    break;

  case 32:
#line 263 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = (CTBNDLvsp[0].expr);
}
#line 1709 "BooleanGrammar.tab.c"
    break;

  case 33:
#line 267 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new AddExpression((CTBNDLvsp[-2].expr), (CTBNDLvsp[0].expr));
}
#line 1717 "BooleanGrammar.tab.c"
    break;

  case 34:
#line 271 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new SubExpression((CTBNDLvsp[-2].expr), (CTBNDLvsp[0].expr));
}
#line 1725 "BooleanGrammar.tab.c"
    break;

  case 35:
#line 277 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = (CTBNDLvsp[0].expr);
}
#line 1733 "BooleanGrammar.tab.c"
    break;

  case 36:
#line 281 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new LetterExpression((CTBNDLvsp[-2].expr), (CTBNDLvsp[0].expr));
}
#line 1741 "BooleanGrammar.tab.c"
    break;

  case 37:
#line 285 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new GreaterExpression((CTBNDLvsp[-2].expr), (CTBNDLvsp[0].expr));
}
#line 1749 "BooleanGrammar.tab.c"
    break;

  case 38:
#line 289 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new LetterOrEqualExpression((CTBNDLvsp[-2].expr), (CTBNDLvsp[0].expr));
}
#line 1757 "BooleanGrammar.tab.c"
    break;

  case 39:
#line 293 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new GreaterOrEqualExpression((CTBNDLvsp[-2].expr), (CTBNDLvsp[0].expr));
}
#line 1765 "BooleanGrammar.tab.c"
    break;

  case 40:
#line 299 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = (CTBNDLvsp[0].expr);
}
#line 1773 "BooleanGrammar.tab.c"
    break;

  case 41:
#line 303 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new EqualExpression((CTBNDLvsp[-2].expr), (CTBNDLvsp[0].expr));
}
#line 1781 "BooleanGrammar.tab.c"
    break;

  case 42:
#line 307 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new NotEqualExpression((CTBNDLvsp[-2].expr), (CTBNDLvsp[0].expr));
}
#line 1789 "BooleanGrammar.tab.c"
    break;

  case 43:
#line 313 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = (CTBNDLvsp[0].expr);
}
#line 1797 "BooleanGrammar.tab.c"
    break;

  case 44:
#line 317 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new AndLogicalExpression((CTBNDLvsp[-2].expr), (CTBNDLvsp[0].expr));
}
#line 1805 "BooleanGrammar.tab.c"
    break;

  case 45:
#line 323 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = (CTBNDLvsp[0].expr);
}
#line 1813 "BooleanGrammar.tab.c"
    break;

  case 46:
#line 327 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new OrLogicalExpression((CTBNDLvsp[-2].expr), (CTBNDLvsp[0].expr));
}
#line 1821 "BooleanGrammar.tab.c"
    break;

  case 47:
#line 333 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = (CTBNDLvsp[0].expr);
}
#line 1829 "BooleanGrammar.tab.c"
    break;

  case 48:
#line 337 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new XorLogicalExpression((CTBNDLvsp[-2].expr), (CTBNDLvsp[0].expr));
}
#line 1837 "BooleanGrammar.tab.c"
    break;

  case 49:
#line 341 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new XorLogicalExpression((CTBNDLvsp[-2].expr), (CTBNDLvsp[0].expr));
}
#line 1845 "BooleanGrammar.tab.c"
    break;

  case 50:
#line 347 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = (CTBNDLvsp[0].expr);
}
#line 1853 "BooleanGrammar.tab.c"
    break;

  case 51:
#line 351 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = new CondExpression((CTBNDLvsp[-4].expr), (CTBNDLvsp[-2].expr), (CTBNDLvsp[0].expr));
}
#line 1861 "BooleanGrammar.tab.c"
    break;

  case 52:
#line 357 "BooleanGrammar.y"
{
  (CTBNDLval.expr) = (CTBNDLvsp[0].expr);
}
#line 1869 "BooleanGrammar.tab.c"
    break;


#line 1873 "BooleanGrammar.tab.c"

      default: break;
    }
  /* User semantic actions sometimes alter CTBNDLchar, and that requires
     that CTBNDLtoken be updated with the new translation.  We take the
     approach of translating immediately before every use of CTBNDLtoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering CTBNDLchar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", CTBNDLr1[CTBNDLn], &CTBNDLval, &CTBNDLloc);

  YYPOPSTACK (CTBNDLlen);
  CTBNDLlen = 0;
  YY_STACK_PRINT (CTBNDLss, CTBNDLssp);

  *++CTBNDLvsp = CTBNDLval;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */
  {
    const int CTBNDLlhs = CTBNDLr1[CTBNDLn] - YYNTOKENS;
    const int CTBNDLi = CTBNDLpgoto[CTBNDLlhs] + *CTBNDLssp;
    CTBNDLstate = (0 <= CTBNDLi && CTBNDLi <= YYLAST && CTBNDLcheck[CTBNDLi] == *CTBNDLssp
               ? CTBNDLtable[CTBNDLi]
               : CTBNDLdefgoto[CTBNDLlhs]);
  }

  goto CTBNDLnewstate;


/*--------------------------------------.
| CTBNDLerrlab -- here on detecting error.  |
`--------------------------------------*/
CTBNDLerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  CTBNDLtoken = CTBNDLchar == YYEMPTY ? YYEMPTY : YYTRANSLATE (CTBNDLchar);

  /* If not already recovering from an error, report this error.  */
  if (!CTBNDLerrstatus)
    {
      ++CTBNDLnerrs;
#if ! YYERROR_VERBOSE
      CTBNDLerror (YY_("syntax error"));
#else
# define YYSYNTAX_ERROR CTBNDLsyntax_error (&CTBNDLmsg_alloc, &CTBNDLmsg, \
                                        CTBNDLssp, CTBNDLtoken)
      {
        char const *CTBNDLmsgp = YY_("syntax error");
        int CTBNDLsyntax_error_status;
        CTBNDLsyntax_error_status = YYSYNTAX_ERROR;
        if (CTBNDLsyntax_error_status == 0)
          CTBNDLmsgp = CTBNDLmsg;
        else if (CTBNDLsyntax_error_status == 1)
          {
            if (CTBNDLmsg != CTBNDLmsgbuf)
              YYSTACK_FREE (CTBNDLmsg);
            CTBNDLmsg = YY_CAST (char *, YYSTACK_ALLOC (YY_CAST (YYSIZE_T, CTBNDLmsg_alloc)));
            if (!CTBNDLmsg)
              {
                CTBNDLmsg = CTBNDLmsgbuf;
                CTBNDLmsg_alloc = sizeof CTBNDLmsgbuf;
                CTBNDLsyntax_error_status = 2;
              }
            else
              {
                CTBNDLsyntax_error_status = YYSYNTAX_ERROR;
                CTBNDLmsgp = CTBNDLmsg;
              }
          }
        CTBNDLerror (CTBNDLmsgp);
        if (CTBNDLsyntax_error_status == 2)
          goto CTBNDLexhaustedlab;
      }
# undef YYSYNTAX_ERROR
#endif
    }



  if (CTBNDLerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (CTBNDLchar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (CTBNDLchar == YYEOF)
            YYABORT;
        }
      else
        {
          CTBNDLdestruct ("Error: discarding",
                      CTBNDLtoken, &CTBNDLlval);
          CTBNDLchar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto CTBNDLerrlab1;


/*---------------------------------------------------.
| CTBNDLerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
CTBNDLerrorlab:
  /* Pacify compilers when the user code never invokes YYERROR and the
     label CTBNDLerrorlab therefore never appears in user code.  */
  if (0)
    YYERROR;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (CTBNDLlen);
  CTBNDLlen = 0;
  YY_STACK_PRINT (CTBNDLss, CTBNDLssp);
  CTBNDLstate = *CTBNDLssp;
  goto CTBNDLerrlab1;


/*-------------------------------------------------------------.
| CTBNDLerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
CTBNDLerrlab1:
  CTBNDLerrstatus = 3;      /* Each real token shifted decrements this.  */

  for (;;)
    {
      CTBNDLn = CTBNDLpact[CTBNDLstate];
      if (!CTBNDLpact_value_is_default (CTBNDLn))
        {
          CTBNDLn += YYTERROR;
          if (0 <= CTBNDLn && CTBNDLn <= YYLAST && CTBNDLcheck[CTBNDLn] == YYTERROR)
            {
              CTBNDLn = CTBNDLtable[CTBNDLn];
              if (0 < CTBNDLn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (CTBNDLssp == CTBNDLss)
        YYABORT;


      CTBNDLdestruct ("Error: popping",
                  CTBNDLstos[CTBNDLstate], CTBNDLvsp);
      YYPOPSTACK (1);
      CTBNDLstate = *CTBNDLssp;
      YY_STACK_PRINT (CTBNDLss, CTBNDLssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++CTBNDLvsp = CTBNDLlval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", CTBNDLstos[CTBNDLn], CTBNDLvsp, CTBNDLlsp);

  CTBNDLstate = CTBNDLn;
  goto CTBNDLnewstate;


/*-------------------------------------.
| CTBNDLacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
CTBNDLacceptlab:
  CTBNDLresult = 0;
  goto CTBNDLreturn;


/*-----------------------------------.
| CTBNDLabortlab -- YYABORT comes here.  |
`-----------------------------------*/
CTBNDLabortlab:
  CTBNDLresult = 1;
  goto CTBNDLreturn;


#if !defined CTBNDLoverflow || YYERROR_VERBOSE
/*-------------------------------------------------.
| CTBNDLexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
CTBNDLexhaustedlab:
  CTBNDLerror (YY_("memory exhausted"));
  CTBNDLresult = 2;
  /* Fall through.  */
#endif


/*-----------------------------------------------------.
| CTBNDLreturn -- parsing is finished, return the result.  |
`-----------------------------------------------------*/
CTBNDLreturn:
  if (CTBNDLchar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      CTBNDLtoken = YYTRANSLATE (CTBNDLchar);
      CTBNDLdestruct ("Cleanup: discarding lookahead",
                  CTBNDLtoken, &CTBNDLlval);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (CTBNDLlen);
  YY_STACK_PRINT (CTBNDLss, CTBNDLssp);
  while (CTBNDLssp != CTBNDLss)
    {
      CTBNDLdestruct ("Cleanup: popping",
                  CTBNDLstos[+*CTBNDLssp], CTBNDLvsp);
      YYPOPSTACK (1);
    }
#ifndef CTBNDLoverflow
  if (CTBNDLss != CTBNDLssa)
    YYSTACK_FREE (CTBNDLss);
#endif
#if YYERROR_VERBOSE
  if (CTBNDLmsg != CTBNDLmsgbuf)
    YYSTACK_FREE (CTBNDLmsg);
#endif
  return CTBNDLresult;
}
#line 366 "BooleanGrammar.y"


#include "lex.CTBNDL.cc"

void set_current_network(Network* network)
{
  current_network = network;
}

Network* get_current_network()
{
  return current_network;
}
