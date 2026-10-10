// Stamps the quarter icon and version info onto the Windows build.
import * as ResEdit from 'resedit';
import * as PELibrary from 'pe-library';
import fs from 'fs';
const exePath='dist/Call-it/Call-it-win_x64.exe';
const exe=PELibrary.NtExecutable.from(fs.readFileSync(exePath),{ignoreCert:true});
const res=PELibrary.NtExecutableResource.from(exe);
const iconFile=ResEdit.Data.IconFile.from(fs.readFileSync('icon.ico'));
ResEdit.Resource.IconGroupEntry.replaceIconsForResource(res.entries,1,1033,iconFile.icons.map(i=>i.data));
const vi=ResEdit.Resource.VersionInfo.createEmpty();
vi.setFileVersion(1,0,0,0,1033);vi.setProductVersion(1,0,0,0,1033);
vi.setStringValues({lang:1033,codepage:1200},{FileDescription:'Call it.',ProductName:'Call it.',CompanyName:'Call it',OriginalFilename:'Call-it.exe',LegalCopyright:''});
vi.outputToResourceEntries(res.entries);
res.outputResource(exe);
fs.writeFileSync('Call-it.exe',Buffer.from(exe.generate()));
console.log('wrote Call-it.exe');
