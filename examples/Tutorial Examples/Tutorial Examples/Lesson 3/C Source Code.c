#include <ExternalInterface.h>

// deal with A4

#ifdef THINK_C
	#include <SetupA4.h>
	#define	EnterCodeResource() do { RememberA0(); SetUpA4(); } while (0)
	#define ExitCodeResource() do { RestoreA4(); } while (0)
#endif
#ifdef __MWERKS__
	#include <A4Stuff.h>
#endif

#include <Aliases.h>
#include <string.h>

pascal OSErr main(ExternalCallbackBlock *callbacks, WindowPtr w, long flags, AppleEvent *event, AppleEvent *reply)
{
	OSErr	err = noErr;
	EnterCodeResource();
	{
		Handle text;
	
		short count = 0;
		StandardFileReply **files = nil;
		
		if (event == nil)
		{
			if (! bbxtOpenSeveral(callbacks, FALSE, &count, &files))
				err = userCanceledErr;
		}
		else
		{
			err = errAEEventNotHandled;	//	sorry...
		}
		
		if (err == noErr)
		{
			short	i;
				
			long	total;
			long	offset;
			
			StandardFileReply	*reply;
			
			HLockHi((Handle)files);
			
			//	spin through all of the files, resolve aliases, and figure out how
			//	much space we need.
			
			for (i = 0, total = 0, reply = *files; (err == noErr) && (i < count); i++, reply++)
			{
	 			if (reply->sfFlags & 0x8000)
				{
					Boolean	scratch;
					
					err = ResolveAliasFile(&reply->sfFile, TRUE, &scratch, &scratch);
				}
				
				if (err == noErr)
				{
					CInfoPBRec	cpb;
					
					memset(&cpb, 0, sizeof(CInfoPBRec));
					cpb.hFileInfo.ioNamePtr = reply->sfFile.name;
					cpb.hFileInfo.ioVRefNum = reply->sfFile.vRefNum;
					cpb.hFileInfo.ioDirID = reply->sfFile.parID;
					
					err = PBGetCatInfoSync(&cpb);
					if (err == noErr)
						total += cpb.hFileInfo.ioFlLgLen;
				}
			}
			
			if (total > 0)
			{
				if (err == noErr)
				{
					text = bbxtAllocate(callbacks, total, FALSE);
					if (text == nil)
						err = memFullErr;
				}
				
				//	now, read in the files. Note that if an error occurred, we won't
				//	enter this loop at all.
				
				for (i = 0, offset = 0, reply = *files; (err == noErr) && (i < count); i++, reply++)
				{
					short	path;
					
					err = HOpen(reply->sfFile.vRefNum, reply->sfFile.parID, reply->sfFile.name, fsRdPerm, &path);
					if (err == noErr)
					{
						long	count;
						unsigned char *dst = ((unsigned char *)(*text)) + offset;
						
						GetEOF(path, &count);
						err = FSRead(path, &count, dst);
						
						if (bbxtGetCallbackVersion(callbacks) >= 7)
							bbxtFilterLineFeeds(callbacks, dst, &count);
						
						offset += count;
						
						FSClose(path);
					}
				}
					
				//	because FilterLineFeeds() may have reduced the amount of text, we
				//	may need to shrink the handle a bit so that there's not junk off the
				//	end.
				
				SetHandleSize(text, offset);
	
				//	we're done with the files...
				DisposeHandle((Handle)files);
				
				if (offset)
				{
					w = bbxtNewDocument(callbacks);
					bbxtSetWindowContents(callbacks, w, text);
				}
			}
		}
	}
		ExitCodeResource();
	
	return err;
}
