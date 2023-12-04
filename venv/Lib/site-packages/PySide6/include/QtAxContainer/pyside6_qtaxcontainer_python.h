// Copyright (C) 2022 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only


#ifndef SBK_QTAXCONTAINER_PYTHON_H
#define SBK_QTAXCONTAINER_PYTHON_H

#include <sbkpython.h>
#include <sbkconverter.h>
// Module Includes
#include <pyside6_qtwidgets_python.h>
#include <pyside6_qtgui_python.h>
#include <pyside6_qtcore_python.h>

// Bound library includes
#include <QtAxContainer/qaxbase.h>
#include <QtAxContainer/qaxscript.h>
#include <QtAxContainer/qaxselect.h>
class QAxBaseObject;
class QAxBaseWidget;
class QAxObject;
class QAxObjectInterface;
class QAxScriptManager;
class QAxWidget;
// Type indices
enum : int {
    SBK_QAXBASE_IDX                                          = 0,
    SBK_QAXBASEOBJECT_IDX                                    = 1,
    SBK_QAXBASEWIDGET_IDX                                    = 2,
    SBK_QAXOBJECT_IDX                                        = 3,
    SBK_QAXOBJECTINTERFACE_IDX                               = 4,
    SBK_QAXSCRIPT_FUNCTIONFLAGS_IDX                          = 6,
    SBK_QAXSCRIPT_IDX                                        = 5,
    SBK_QAXSCRIPTENGINE_STATE_IDX                            = 8,
    SBK_QAXSCRIPTENGINE_IDX                                  = 7,
    SBK_QAXSCRIPTMANAGER_IDX                                 = 9,
    SBK_QAXSELECT_SANDBOXINGLEVEL_IDX                        = 11,
    SBK_QAXSELECT_IDX                                        = 10,
    SBK_QAXWIDGET_IDX                                        = 12,
    SBK_QtAxContainer_IDX_COUNT                              = 13
};
// This variable stores all Python types exported by this module.
extern PyTypeObject **SbkPySide6_QtAxContainerTypes;

// This variable stores the Python module object exported by this module.
extern PyObject *SbkPySide6_QtAxContainerModuleObject;

// This variable stores all type converters exported by this module.
extern SbkConverter **SbkPySide6_QtAxContainerTypeConverters;

// Converter indices
enum : int {
    SBK_QTAXCONTAINER_QLIST_INT_IDX                          = 0, // QList<int>
    SBK_QTAXCONTAINER_QLIST_QVARIANT_IDX                     = 1, // QList<QVariant>
    SBK_QTAXCONTAINER_QLIST_QOBJECTPTR_IDX                   = 2, // QList<QObject*>
    SBK_QTAXCONTAINER_QLIST_QBYTEARRAY_IDX                   = 3, // QList<QByteArray>
    SBK_QTAXCONTAINER_QLIST_QACTIONPTR_IDX                   = 4, // QList<QAction*>
    SBK_QTAXCONTAINER_QMAP_QSTRING_QVARIANT_IDX              = 5, // QMap<QString,QVariant>
    SBK_QTAXCONTAINER_QLIST_QSTRING_IDX                      = 6, // QList<QString>
    SBK_QtAxContainer_CONVERTERS_IDX_COUNT                   = 7
};
// Macros for type check

QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace Shiboken
{

// PyType functions, to get the PyObjectType for a type T
template<> inline PyTypeObject *SbkType< ::QAxBase >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtAxContainerTypes[SBK_QAXBASE_IDX]); }
template<> inline PyTypeObject *SbkType< ::QAxBaseObject >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtAxContainerTypes[SBK_QAXBASEOBJECT_IDX]); }
template<> inline PyTypeObject *SbkType< ::QAxBaseWidget >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtAxContainerTypes[SBK_QAXBASEWIDGET_IDX]); }
template<> inline PyTypeObject *SbkType< ::QAxObject >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtAxContainerTypes[SBK_QAXOBJECT_IDX]); }
template<> inline PyTypeObject *SbkType< ::QAxObjectInterface >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtAxContainerTypes[SBK_QAXOBJECTINTERFACE_IDX]); }
template<> inline PyTypeObject *SbkType< ::QAxScript::FunctionFlags >() { return SbkPySide6_QtAxContainerTypes[SBK_QAXSCRIPT_FUNCTIONFLAGS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QAxScript >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtAxContainerTypes[SBK_QAXSCRIPT_IDX]); }
template<> inline PyTypeObject *SbkType< ::QAxScriptEngine::State >() { return SbkPySide6_QtAxContainerTypes[SBK_QAXSCRIPTENGINE_STATE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QAxScriptEngine >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtAxContainerTypes[SBK_QAXSCRIPTENGINE_IDX]); }
template<> inline PyTypeObject *SbkType< ::QAxScriptManager >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtAxContainerTypes[SBK_QAXSCRIPTMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QAxSelect::SandboxingLevel >() { return SbkPySide6_QtAxContainerTypes[SBK_QAXSELECT_SANDBOXINGLEVEL_IDX]; }
template<> inline PyTypeObject *SbkType< ::QAxSelect >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtAxContainerTypes[SBK_QAXSELECT_IDX]); }
template<> inline PyTypeObject *SbkType< ::QAxWidget >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtAxContainerTypes[SBK_QAXWIDGET_IDX]); }

} // namespace Shiboken

QT_WARNING_POP
#endif // SBK_QTAXCONTAINER_PYTHON_H

